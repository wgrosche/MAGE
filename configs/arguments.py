import sys
import argparse
import os

from configs.utils import read_yaml_file, convert_yaml_dict_to_arg_list, fill_dict_with_missing_value, aug_tuple
from configs.utils import args_to_dict
from utils.log_utils import log, set_log_level, dict_to_string


parser = argparse.ArgumentParser(description='Process some integers.')

#add argument group for calib, ann, train, infer and track
parser_main = parser.add_argument_group("main")
parser_calib = parser.add_argument_group("calibration")
parser_ann = parser.add_argument_group("annotation")
parser_train = parser.add_argument_group("training")
parser_infer = parser.add_argument_group("inference")
parser_track = parser.add_argument_group("tracking")

parser_main.add_argument("-cfg", "--config_file", dest="config_file", help="Path to a YAML file containing of argument that will be used as new default value, if command line argument are specified they will override the value from the YAML file", type=str, default="/root/project_config.yaml")
# parser.add_argument("-l", "--log_lvl", dest="log_lvl", default="debug", choices=["debug", "spam", "verbose", "info", "warning", "error"], help='Set level of logger to get more or less verbose output')
# parser.add_argument("-dr", "--data_root", dest="data_root", help="Path to the data folder", type=str, default=None)
# parser_main.add_argument("-cfg", "--config_file", dest="config_file", help="Path to a YAML file containing of argument that will be used as new default value, if command line argument are specified they will override the value from the YAML file", type=str, default="./project_config.yaml")
parser_main.add_argument("-l", "--log_lvl", dest="log_lvl", default="debug", choices=["debug", "spam", "verbose", "info", "warning", "error"], help='Set level of logger to get more or less verbose output')
parser_main.add_argument("-dr", "--data_root", dest="data_root", help="Path to the data folder", type=str, default=None)
parser_main.add_argument("-data", "--data", dest="data", help="Path to the raw footage to be symlinked", type=str, default=None)
parser_main.add_argument("-cr", "--code_root", dest="code_root", help="Path to the code folder", type=str, default=None)

####### Calibration #######
parser_calib.add_argument("-fi", "--force_intrinsics", dest="force_intrinsics", action="store_true", help="Force recalculation of intrinsics from footage",)
parser_calib.add_argument("-fr", "--force_reconstruction", dest="force_reconstruction", action="store_true", help="Force OpenSfM reconstruction", default=False)
parser_calib.add_argument("-osfmr", "--opensfm_repo", dest="opensfm_repo", help="Location of OpenSfM_Repo", type=str, default="/OpenSfM")
parser_calib.add_argument("-omni", "--omni_tag", dest="omni_tag", help="Tag to identify omnidirectional camera", type=str, default="360")
parser_calib.add_argument("--focal_length", dest="focal_length", help="Default focal length to add to image metadata in mm", type=str, default="507")
parser_calib.add_argument("-focal", "--default_focal", dest="default_focal", help="Default normalised focal length for camera overrides in opensfm", type=float, default=0.45)
parser_calib.add_argument("-uau", "--use_alpha_undistort", dest="use_alpha_undistort", default=False, action="store_true", help="When undistorting images, preserve edges by using alpha calibration value")

# parser_calib

####### Annotation #######
parser_ann.add_argument("-nt", "--num_train_sample", dest="num_train_sample", help="Number of training sample", type=int, default=1000)
parser_ann.add_argument("-vl", "--val_seq_length", dest="val_seq_length", help="Length of validation sequence (in nb of frame)", type=int, default=100)

####### Training #######
# parser_train
parser_train.add_argument("-tcfg", "--train_config_file", dest="train_config_file", help="Path to a YAML file containing of argument that will be used to override default training parameter defined in code/detection/configs/arguments.py", type=str, default=None)


####### Inference #######
# parser_infer

####### Tracking #######
# parser_track

def get_config_dict():
    """
    Generate config dict from command line argument and config file if existing_conf_dict is not None, value are added to the existing dict if they are not already defined, 
    """

    log.spam(f'Original command {" ".join(sys.argv)}')
    # args = parser.parse_args()
    args, unknown = parser.parse_known_args(sys.argv[1:])

    if args.config_file is not None or "pomelo_cfg" in os.environ:
        config_path = os.environ.get('pomelo_cfg') if "pomelo_cfg" in os.environ else args.config_file

        yaml_dict = read_yaml_file(config_path)
        arg_list = convert_yaml_dict_to_arg_list(yaml_dict)

        # args = parser.parse_args(arg_list + sys.argv[1:])
        args, unknown = parser.parse_known_args(arg_list + sys.argv[1:])

    args_dict = args_to_dict(parser, args)

    config = {p_type:args_dict[p_type] for p_type in ["main", "calibration", "annotation", "training", "inference", "tracking"]}
    set_log_level(config["main"]["log_lvl"])
    
    return config


if __name__ == '__main__':
    conf_dict = get_config_dict()
