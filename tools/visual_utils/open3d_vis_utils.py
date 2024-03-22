"""
Open3d visualization tool box
Written by Jihan YANG
All rights preserved from 2021 - present.
"""
import open3d
import torch
import matplotlib
import numpy as np
from pcdet.ops.iou3d_nms import iou3d_nms_utils
box_colormap = [
    [1, 1, 1],
    [0, 1, 0],
    [0, 1, 1],
    [1, 1, 0],
]


def get_coor_colors(obj_labels):
    """
    Args:
        obj_labels: 1 is ground, labels > 1 indicates different instance cluster

    Returns:
        rgb: [N, 3]. color for each point.
    """
    colors = matplotlib.colors.XKCD_COLORS.values()
    max_color_num = obj_labels.max()

    color_list = list(colors)[:max_color_num+1]
    colors_rgba = [matplotlib.colors.to_rgba_array(color) for color in color_list]
    label_rgba = np.array(colors_rgba)[obj_labels]
    label_rgba = label_rgba.squeeze()[:, :3]

    return label_rgba


def draw_scenes(points, gt_boxes=None, ref_boxes=None, ref_labels=None, ref_scores=None, point_colors=None, draw_origin=True,shijiao =None):
    if isinstance(points, torch.Tensor):
        points = points.cpu().numpy()
    if isinstance(gt_boxes, torch.Tensor):
        gt_boxes = gt_boxes.cpu().numpy()
    if isinstance(ref_boxes, torch.Tensor):
        ref_boxes = ref_boxes.cpu().numpy()
    print(type(ref_boxes))
    #if gt_boxes!=None:
    if len(ref_boxes)!=0 and len(gt_boxes)!=0:
        print(iou3d_nms_utils.boxes_iou3d_gpu(torch.tensor(gt_boxes[:,:7]).cuda(), torch.tensor(ref_boxes).cuda()))
    print(ref_labels)
    print('true',gt_boxes)
    vis = open3d.visualization.Visualizer()
    vis.create_window()
    #view_control = vis.get_view_control()
    vis.get_render_option().point_size = 2.0
    vis.get_render_option().background_color = np.zeros(3)
    
    # draw origin
    if draw_origin:
        axis_pcd = open3d.geometry.TriangleMesh.create_coordinate_frame(size=1.0, origin=[0, 0, 0])
        vis.add_geometry(axis_pcd)

    pts = open3d.geometry.PointCloud()
    pts.points = open3d.utility.Vector3dVector(points[:, :3])

    vis.add_geometry(pts)
    ctr2 = vis.get_view_control()
    if point_colors is None:
        pts.colors = open3d.utility.Vector3dVector(np.ones((points.shape[0], 3)))
    else:
        pts.colors = open3d.utility.Vector3dVector(point_colors)

    if gt_boxes is not None:
        vis = draw_box(vis, gt_boxes, (0, 0, 1))

    if ref_boxes is not None:
        vis = draw_box(vis, ref_boxes, (0, 1, 0), ref_labels, ref_scores)
    if shijiao is not None:
        
        ctr2.convert_from_pinhole_camera_parameters(shijiao)
        #print('sssd')
    #view_control.set_lookat([0.0, 0.0, 0.0])
    #view_control.set_up([-1, -1, 0])
    #view_control.set_front([1, 0, 1])
    ctr2.set_zoom(0.5)
    #ctr = vis.get_view_control()
    
    vis.run()
    params = ctr2.convert_to_pinhole_camera_parameters()
    #print('ddddd',params.intrinsic.intrinsic_matrix)
    vis.capture_screen_image('/media/newdisk/liuqifeng/IASSD_liu/IASSD57_2_newdisk/tools/dd.jpg',do_render=True)
    vis.destroy_window()
    return params


def translate_boxes_to_open3d_instance(gt_boxes):
    """
             4-------- 6
           /|         /|
          5 -------- 3 .
          | |        | |
          . 7 -------- 1
          |/         |/
          2 -------- 0
    """
    center = gt_boxes[0:3]
    lwh = gt_boxes[3:6]
    axis_angles = np.array([0, 0, gt_boxes[6] + 1e-10])
    rot = open3d.geometry.get_rotation_matrix_from_axis_angle(axis_angles)
    box3d = open3d.geometry.OrientedBoundingBox(center, rot, lwh)

    line_set = open3d.geometry.LineSet.create_from_oriented_bounding_box(box3d)

    # import ipdb; ipdb.set_trace(context=20)
    lines = np.asarray(line_set.lines)
    lines = np.concatenate([lines, np.array([[1, 4], [7, 6]])], axis=0)

    line_set.lines = open3d.utility.Vector2iVector(lines)



    # mat = open3d.visualization.rendering.MaterialRecord()
    # mat.shader = "unlitLine"
    # mat.line_width = 10  # note that this is scaled with respect to pixels,
    # # so will give different results depending on the
    # # scaling values of your system
    # open3d.visualization.draw({
    #     "name": "lines",
    #     "geometry": line_set,
    #     "material": mat
    # })


    return line_set, box3d


def draw_box(vis, gt_boxes, color=(0, 1, 0), ref_labels=None, score=None):
    for i in range(gt_boxes.shape[0]):
        line_set, box3d = translate_boxes_to_open3d_instance(gt_boxes[i])
        if ref_labels is None:
            line_set.paint_uniform_color(color)
        else:
            line_set.paint_uniform_color(box_colormap[ref_labels[i]])

        vis.add_geometry(line_set)
        
        # if score is not None:
        #     corners = box3d.get_box_points()
        #     vis.add_3d_label(corners[5], '%.2f' % score[i])
    return vis
