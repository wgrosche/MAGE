import argparse

def str2bool(v):
        if v.lower() in ('yes', 'true', 't', 'y', '1'):
            return True
        elif v.lower() in ('no', 'false', 'f', 'n', '0'):
            return False
        else:
            raise argparse.ArgumentTypeError('Boolean value expected.')

class Arguments():

    def __init__(self):
        self.parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        self.initialize()

    def initialize(self):
        # arguments required for compute_intrinsics.py
        self.parser.add_argument("--intrinsics_frame_rate", "-ifr", type=int, 
                                 default=0.9, required=False, 
                                 help="Frame rate for frame extraction in intrinsics calc.")
        
        self.parser.add_argument("--description", "-d", type=str, default="", 
                                 required=False, 
                                 help="Optional description to add to the output file.")
        
        self.parser.add_argument("--inner_corners_height", "-ich", type=int, 
                                 default=6, 
                                 help="Number of inner corners on the shortest edge of the checkerboard.")
        
        self.parser.add_argument("--inner_corners_width", "-icw", type=int, 
                                 default=9, 
                                 help="Number of inner corners on the longest edge of the checkerboard.")
        
        self.parser.add_argument("--square_sizes", "-s", type=int, default=40, 
                                 required=False, help="Size of the squares")
        
        self.parser.add_argument("--alpha", "-a", type=float, default=0.90, 
                                 required=False, 
                                 help="Parameter controlling the ammount of out-of-image pixels (\"black regions\") retained in the undistorted image.")
        
        self.parser.add_argument("--threads", "-t", type=int, default=4, 
                                 required=False)
        
        self.parser.add_argument("--force_monotonicity", "-fm", type=str2bool, 
                                 default=False, required=False, 
                                 help="Force monotonicity in the range defined by monotonic_range. To be used only in extreme cases.")
        
        self.parser.add_argument("--monotonic_range", "-mr", type=float, 
                                 default=-1, required=False, 
                                 help=("Value defining the range for the distortion must be monotonic. "
                                   "Typical value to try 1.3. Be careful: increasing this value may negatively perturb the distortion function."))
        
        self.parser.add_argument("--rational_model", "-rm", action="store_false", 
                                 required=False, 
                                 help="Use a camera model that is better suited for wider lenses.")
        
        self.parser.add_argument("--fix_principal_point", "-fpp", 
                                 action="store_true", required=False, 
                                 help="Fix the principal point either at the center of the image or as specified by intrisic guess.")
        
        self.parser.add_argument("--fix_aspect_ratio", "-far", 
                                 action="store_true", required=False) 
        
        self.parser.add_argument("--zero_tangent_dist", "-ztg", 
                                 action="store_true", required=False) 
        
        self.parser.add_argument("--criteria_eps", "-eps", type=float, 
                                 default=1e-5, required=False, 
                                 help="Precision criteria. A larger value can prevent overfitting and artifacts on the borders.")
        
        self.parser.add_argument("--fix_k1", "-k1", action="store_true", 
                                 required=False)
        
        self.parser.add_argument("--fix_k2", "-k2", action="store_true", 
                                 required=False)
        
        self.parser.add_argument("--fix_k3", "-k3", action="store_true", 
                                 required=False)
        
        self.parser.add_argument("--fix_k4", "-k4", action="store_true", 
                                 required=False)
        
        self.parser.add_argument("--fix_k5", "-k5", action="store_true", 
                                 required=False)
        
        self.parser.add_argument("--fix_k6", "-k6", action="store_true", 
                                 required=False)
        
        self.parser.add_argument("--intrinsic_guess", "-ig", type=str, 
                                 required=False, default="", 
                                 help="JSON file containing a initial guesses for the intrinsic matrix and distortion parameters.")
        
        self.parser.add_argument("--save_keypoints", action="store_true", 
                                 required=False)
        
        self.parser.add_argument("--load_keypoints", action="store_true", 
                                 required=False)
        
        self.parser.add_argument("--debug", action="store_true", required=False)


     

    def parse(self):
        self.args = self.parser.parse_args("")
        return self.args
    