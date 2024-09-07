# def load_scene_contacts(dataset_folder, test_split_only=False, num_test=None, scene_contacts_path='scene_contacts_new'):
# class PointCloudReader:
    # def get_scene_batch(self, scene_idx=None, return_segmap=False, save=False):
    # start at this definition because we already have the scene point clouds
# modify these two definitions to load custom data in my format


def load_scene_contacts(dataset_folder, test_split_only=False, num_test=None, scene_contacts_path='scene_contacts_new'):
    """
    Load contact grasp annotations from acronym scenes 

    Arguments:
        dataset_folder {str} -- folder with acronym data and scene contacts

    Keyword Arguments:
        test_split_only {bool} -- whether to only return test split scenes (default: {False})
        num_test {int} -- how many test scenes to use (default: {None})
        scene_contacts_path {str} -- name of folder with scene contact grasp annotations (default: {'scene_contacts_new'})

    Returns:
        list(dicts) -- list of scene annotations dicts with object paths and transforms and grasp contacts and transforms.
    """
    pass

def load_labels_and_losses(grasp_estimator, contact_infos, global_config, train=True):
    """
    Loads labels to memory and builds graph for computing losses

    Arguments:
        grasp_estimator {class} -- Grasp Estimator Instance
        contact_infos {list(dicts)} -- Per scene mesh: grasp contact information  
        global_config {dict} -- global config

    Keyword Arguments:
        train {bool} -- training mode (default: {True})

    Returns:
        dict[str:tf.variables] -- tf references to labels and losses
    """
    pass

    def load_contact_grasps(contact_list, data_config):
        """
        Loads fixed amount of contact grasp data per scene into tf CPU/GPU memory

        Arguments:
            contact_infos {list(dicts)} -- Per scene mesh: grasp contact information  
            data_config {dict} -- data config

        Returns:
            [tf_pos_contact_points, tf_pos_contact_dirs, tf_pos_contact_offsets, 
            tf_pos_contact_approaches, tf_pos_finger_diffs, tf_scene_idcs, 
            all_obj_paths, all_obj_transforms] -- tf.constants with per scene grasp data, object paths/transforms in scene
        """
        return tf_pos_contact_points, tf_pos_contact_dirs, tf_pos_contact_approaches, tf_pos_finger_diffs, tf_scene_idcs
    




def train(global_config, log_dir):
    """
    Trains Contact-GraspNet

    Arguments:
        global_config {dict} -- config dict
        log_dir {str} -- Checkpoint directory
    """

    contact_infos = load_scene_contacts(global_config['DATA']['data_path'],
                                        scene_contacts_path=global_config['DATA']['scene_contacts_path'])
    pcreader = PointCloudReader(
        root_folder=global_config['DATA']['data_path'],
        batch_size=global_config['OPTIMIZER']['batch_size'],
        estimate_normals=global_config['DATA']['input_normals'],
        raw_num_points=global_config['DATA']['raw_num_points'],
        use_uniform_quaternions = global_config['DATA']['use_uniform_quaternions'],
        scene_obj_scales = [c['obj_scales'] for c in contact_infos],
        scene_obj_paths = [c['obj_paths'] for c in contact_infos],
        scene_obj_transforms = [c['obj_transforms'] for c in contact_infos],
        num_train_samples = num_train_samples,
        num_test_samples = num_test_samples,
        use_farthest_point = global_config['DATA']['use_farthest_point'],
        intrinsics=global_config['DATA']['intrinsics'],
        elevation=global_config['DATA']['view_sphere']['elevation'],
        distance_range=global_config['DATA']['view_sphere']['distance_range'],
        pc_augm_config=global_config['DATA']['pc_augm'],
        depth_augm_config=global_config['DATA']['depth_augm']
    )
    loss_ops = load_labels_and_losses(grasp_estimator, contact_infos, global_config)
    step = train_one_epoch(sess, ops, summary_ops, file_writers, pcreader)
    eval_validation_scenes(sess, ops, summary_ops, file_writers, pcreader)

def train_one_epoch(sess, ops, summary_ops, file_writers, pcreader):
    """ ops: dict mapping from string to tf ops """
    for batch_idx in range(pcreader._num_train_samples):
        batch_data, cam_poses, scene_idx = pcreader.get_scene_batch(scene_idx=batch_idx)

def eval_validation_scenes(sess, ops, summary_ops, file_writers, pcreader, max_eval_objects=500):
    pass
    loss_log = np.zeros((min(pcreader._num_test_samples, max_eval_objects),7))
    for batch_idx in np.arange(min(pcreader._num_test_samples, max_eval_objects)):
        batch_data, cam_poses, scene_idx = pcreader.get_scene_batch(scene_idx=pcreader._num_train_samples + batch_idx)
        assert scene_idx[0] == (pcreader._num_train_samples + batch_idx)