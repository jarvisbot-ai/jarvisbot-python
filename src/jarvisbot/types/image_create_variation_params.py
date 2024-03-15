# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional, Dict, List, Any
from typing_extensions import Literal, Required, TypedDict

from .._types import FileTypes

__all__ = ["ImageCreateVariationParams"]


class ImageCreateVariationParams(TypedDict, total=False):
    ##52

    prompt: Optional[str]
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
    init_images: Required[List[str]]
    resize_mode: Optional[int]
    image_cfg_scale: Optional[float]
    mask: Optional[str]
    mask_blur_x: Optional[int]
    mask_blur_y: Optional[int]
    mask_blur: Optional[int]
    inpainting_fill: Optional[int]
    inpainting_fill_res: Optional[int]
    inpainting_fill_res_padding: Optional[int]
    inpainting_mask_invert: Optional[int]
    initial_noise_multiplier: Optional[float]
    latent_mask: Optional[str]
    sampler_index: Optional[str]
    include_init_images: Optional[bool]
    script_name: Optional[str]
    script_args: Optional[List[str]]
    send_images: Optional[bool]
    save_images: Optional[bool]
    alwayson_scripts: Optional[Dict[str, Any]]