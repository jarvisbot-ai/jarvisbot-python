# File generated from our OpenAPI spec by Stainless.

from typing import List, Dict, Optional, Any

from .image import Image
from .._models import BaseModel

__all__ = ["ImagesResponse"]


class ImagesParameters(BaseModel):
    prompt: str
    negative_prompt: Optional[str] = None
    batch_size: Optional[int] = None
    steps: Optional[int] = None
    cfg_scale: Optional[float] = None
    width: Optional[int] = None
    height: Optional[int] = None
    seed: Optional[int] = None
    styles: Optional[List[str]] = None
    enable_hr: Optional[bool] = None
    denoising_strength: Optional[float] = None
    firstphase_width: Optional[int] = None
    firstphase_height: Optional[int] = None
    hr_scale: Optional[float] = None
    hr_upscaler: Optional[str] = None
    hr_second_pass_steps: Optional[int] = None
    hr_resize_x: Optional[int] = None
    hr_resize_y: Optional[int] = None
    subseed: Optional[int] = None
    subseed_strength: Optional[int] = None
    seed_resize_from_h: Optional[int] = None
    seed_resize_from_w: Optional[int] = None
    sampler_name: Optional[str] = None
    restore_faces: Optional[bool] = None
    tiling: Optional[bool] = None
    do_not_save_samples: Optional[bool] = None
    do_not_save_grid: Optional[bool] = None
    eta: Optional[float] = None
    s_churn: Optional[float] = None
    s_tmax: Optional[float] = None
    s_tmin: Optional[float] = None
    s_noise: Optional[float] = None
    override_settings: Optional[Dict[str, str]] = None
    override_settings_restore_afterwards: Optional[bool] = None
    script_args: Optional[List[str]] = None
    sampler_index: Optional[str] = None
    script_name: Optional[str] = None
    send_images: Optional[bool] = None
    save_images: Optional[bool] = None
    alwayson_scripts: Optional[Dict[str, Any]] = None
    refiner_checkpoint: Optional[str] = None
    refiner_switch_at: Optional[int] = None
    s_min_uncond: Optional[float] = None
    n_iter: Optional[int] = None
    init_images: Optional[List[str]] = None
    resize_mode: Optional[int] = None
    image_cfg_scale: Optional[float] = None
    mask: Optional[str] = None
    mask_blur_x: Optional[int] = None
    mask_blur_y: Optional[int] = None
    mask_blur: Optional[int] = None
    inpainting_fill: Optional[int] = None
    inpainting_fill_res: Optional[int] = None
    inpainting_fill_res_padding: Optional[int] = None
    inpainting_mask_invert: Optional[int] = None
    initial_noise_multiplier: Optional[float] = None
    latent_mask: Optional[str] = None
    include_init_images: Optional[bool] = None


class ImagesResponse(BaseModel):
    images: List[str]

    parameters: ImagesParameters

    info: str
