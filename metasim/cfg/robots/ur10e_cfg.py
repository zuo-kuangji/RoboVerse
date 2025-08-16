from __future__ import annotations

from typing import Literal

from metasim.utils import configclass

from .base_robot_cfg import BaseActuatorCfg, BaseRobotCfg


@configclass
class Ur10ECfg(BaseRobotCfg):
    """Configuration for the Universal Robots UR10e robot.

    The UR10e is a 6-DOF industrial robotic arm with higher payload capacity
    than the UR5e, designed for heavy-duty applications.
    """

    name: str = "ur10e"
    num_joints: int = 6
    fix_base_link: bool = True

    # Asset paths
    usd_path: str = "roboverse_data/robots/Universal_Robots_UR10e/usd/ur10e.usd"
    urdf_path: str = "roboverse_data/robots/Universal_Robots_UR10e/urdf/ur_description/urdf/ur10e.urdf"
    mjcf_path: str = "roboverse_data/robots/Universal_Robots_UR10e/mjcf/ur10e.xml"

    # Physical properties
    enabled_gravity: bool = False
    enabled_self_collisions: bool = False
    isaacgym_read_mjcf: bool = False  # Use URDF for IsaacLab/IsaacGym

    # Actuator configuration - Based on UR10e joint specifications
    # UR10e has higher torque capacity than UR5e due to larger payload
    actuators: dict[str, BaseActuatorCfg] = {
        "shoulder_pan_joint": BaseActuatorCfg(stiffness=2e5, damping=2e4, velocity_limit=2.094),
        "shoulder_lift_joint": BaseActuatorCfg(stiffness=2e5, damping=2e4, velocity_limit=2.094),
        "elbow_joint": BaseActuatorCfg(stiffness=1.5e5, damping=1e4, velocity_limit=3.142),
        "wrist_1_joint": BaseActuatorCfg(stiffness=1e5, damping=8e3, velocity_limit=6.283),
        "wrist_2_joint": BaseActuatorCfg(stiffness=8e4, damping=6e3, velocity_limit=6.283),
        "wrist_3_joint": BaseActuatorCfg(stiffness=5e4, damping=4e3, velocity_limit=6.283),
    }

    # Joint limits - Based on UR10e actual joint limits (radians)
    # UR10e has same joint ranges as other UR series robots
    joint_limits: dict[str, tuple[float, float]] = {
        "shoulder_pan_joint": (-6.28318, 6.28318),  # ±360°
        "shoulder_lift_joint": (-6.28318, 6.28318),  # ±360°
        "elbow_joint": (-3.14159, 3.14159),  # ±180°
        "wrist_1_joint": (-6.28318, 6.28318),  # ±360°
        "wrist_2_joint": (-6.28318, 6.28318),  # ±360°
        "wrist_3_joint": (-6.28318, 6.28318),  # ±360°
    }

    # End-effector body name - UR tool flange
    ee_body_name: str = "tool0"

    # Default joint positions - UR10e standard home position
    default_joint_positions: dict[str, float] = {
        "shoulder_pan_joint": 0.0,
        "shoulder_lift_joint": -1.5708,  # -90°
        "elbow_joint": 0.0,
        "wrist_1_joint": -1.5708,  # -90°
        "wrist_2_joint": 0.0,
        "wrist_3_joint": 0.0,
    }

    # Control type - All joints use position control
    control_type: dict[str, Literal["position", "effort"]] = {
        "shoulder_pan_joint": "position",
        "shoulder_lift_joint": "position",
        "elbow_joint": "position",
        "wrist_1_joint": "position",
        "wrist_2_joint": "position",
        "wrist_3_joint": "position",
    }

    # UR10e has no gripper by default, gripper can be added separately if needed
    # gripper_open_q = []
    # gripper_close_q = []

    # Motion planning configuration (if CuRobo support is available)
    # curobo_ref_cfg_name: str = "ur10e.yml"
    # curobo_tcp_rel_pos: tuple[float, float, float] = [0.0, 0.0, 0.0]
    # curobo_tcp_rel_rot: tuple[float, float, float] = [0.0, 0.0, 0.0]
