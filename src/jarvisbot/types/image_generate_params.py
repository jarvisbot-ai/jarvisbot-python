# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional, List, Dict, Any
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ImageGenerateParams"]


class ImageGenerateParams(TypedDict, total=False):
    # 50
    prompt: Required[str]
    """A text description of the desired image(s).
    """

    negative_prompt: Optional[str]
    """
    """

    styles: Optional[List[str]]
    """
    """

    seed: Optional[int]
    """
    """
    subseed: Optional[int]
    """
    """
    subseed_strength: Optional[float]
    """
    """
    seed_resize_from_h: Optional[int]
    """
    """
    seed_resize_from_w: Optional[int]
    """
    """
    sampler_name: Optional[str]
    """
    """
    batch_size: Optional[int]

    """
    """
    n_iter: Optional[int]

    steps: Optional[int]
    """
    """
    cfg_scale: Optional[float]
    """
    """
    width: Optional[int]
    """
    """

    height: Optional[int]
    """
    """
    restore_faces: Optional[bool]
    """
    """
    tiling: Optional[bool]
    """
    """
    do_not_save_samples: Optional[bool]
    do_not_save_grid: Optional[bool]
    eta: Optional[float]

    denoising_strength: Optional[float]
    """
    """
    s_min_uncond: Optional[float]
    s_churn: Optional[float]
    s_tmax: Optional[float]
    s_tmin: Optional[float]
    s_noise: Optional[float]

    override_settings: Optional[Dict[str, Any]]
    override_settings_restore_afterwards: Optional[bool]

    refiner_checkpoint: Optional[str]
    refiner_switch_at: Optional[float]

    disable_extra_networks: Optional[bool]
    comments: Optional[str]
    enable_hr: Optional[bool]
    firstphase_width: Optional[int]
    firstphase_height: Optional[int]

    hr_scale: Optional[float]
    """
    """
    hr_upscaler: Optional[str]
    """
    """
    hr_second_pass_steps: Optional[int]
    """
    """
    hr_resize_x: Optional[int]
    """
    """
    hr_resize_y: Optional[int]

    hr_checkpoint_name: Optional[str]
    hr_sampler_name: Optional[str]
    hr_prompt: Optional[str]
    hr_negative_prompt: Optional[str]
    sampler_index: Optional[str]
    script_name: Optional[str]
    script_args: Optional[List[Any]]
    send_images: Optional[bool]
    save_images: Optional[bool]
    alwayson_scripts: Optional[Dict[str, Any]]
