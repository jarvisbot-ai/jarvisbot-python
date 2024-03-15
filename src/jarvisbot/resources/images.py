from __future__ import annotations

from typing import Union, Mapping, Optional, cast, List, Dict, Any
from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import (
    ImagesResponse,
    image_generate_params,
    image_create_variation_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes, FileContent
from .._utils import extract_files, maybe_transform, deepcopy_minimal, file_to_base64
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from .._base_client import (
    make_request_options,
)

__all__ = [
    "Images",
    "AsyncImages",
    "ImagesWithRawResponse",
    "AsyncImagesWithRawResponse",
    "ImagesWithStreamingResponse",
    "AsyncImagesWithStreamingResponse"
]


class Images(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ImagesWithRawResponse:
        return ImagesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ImagesWithStreamingResponse:
        return ImagesWithStreamingResponse(self)

    def create_variation(
            self,
            *,
            init_images: List[FileContent],
            prompt: Optional[str] | NotGiven = NOT_GIVEN,
            negative_prompt: Optional[str] | NotGiven = NOT_GIVEN,
            styles: Optional[List[str]] | NotGiven = NOT_GIVEN,
            seed: Optional[int] | NotGiven = NOT_GIVEN,
            subseed: Optional[int] | NotGiven = NOT_GIVEN,
            subseed_strength: Optional[float] | NotGiven = NOT_GIVEN,
            subseed_enable_extras: Optional[bool] | NotGiven = NOT_GIVEN,
            seed_resize_from_h: Optional[int] | NotGiven = NOT_GIVEN,
            seed_resize_from_w: Optional[int] | NotGiven = NOT_GIVEN,
            sampler_name: Optional[str] | NotGiven = NOT_GIVEN,
            batch_size: Optional[int] | NotGiven = NOT_GIVEN,
            steps: Optional[int] | NotGiven = NOT_GIVEN,
            cfg_scale: Optional[float] | NotGiven = NOT_GIVEN,
            width: Optional[int] | NotGiven = NOT_GIVEN,
            height: Optional[int] | NotGiven = NOT_GIVEN,
            restore_faces: Optional[bool] | NotGiven = NOT_GIVEN,
            tiling: Optional[bool] | NotGiven = NOT_GIVEN,
            do_not_save_samples: Optional[bool] | NotGiven = NOT_GIVEN,
            do_not_save_grid: Optional[bool] | NotGiven = NOT_GIVEN,
            eta: Optional[float] | NotGiven = NOT_GIVEN,
            denoising_strength: Optional[float] | NotGiven = NOT_GIVEN,
            s_min_uncond: Optional[float] | NotGiven = NOT_GIVEN,
            s_churn: Optional[float] | NotGiven = NOT_GIVEN,
            s_tmax: Optional[float] | NotGiven = NOT_GIVEN,
            s_tmin: Optional[float] | NotGiven = NOT_GIVEN,
            s_noise: Optional[float] | NotGiven = NOT_GIVEN,
            override_settings: Optional[Dict[str, Any]] | NotGiven = NOT_GIVEN,
            override_settings_restore_afterwards: Optional[bool] | NotGiven = NOT_GIVEN,
            refiner_checkpoint: Optional[bool] | NotGiven = NOT_GIVEN,
            refiner_switch_at: Optional[float] | NotGiven = NOT_GIVEN,
            disable_extra_networks: Optional[bool] | NotGiven = NOT_GIVEN,
            comments: Optional[Dict[str, Any]] | NotGiven = NOT_GIVEN,
            resize_mode: Optional[int] | NotGiven = NOT_GIVEN,
            image_cfg_scale: Optional[float] | NotGiven = NOT_GIVEN,
            mask_blur_x: Optional[int] | NotGiven = NOT_GIVEN,
            mask_blur_y: Optional[int] | NotGiven = NOT_GIVEN,
            mask_blur: Optional[int] | NotGiven = NOT_GIVEN,
            inpainting_fill: Optional[int] | NotGiven = NOT_GIVEN,
            inpainting_fill_res: Optional[int] | NotGiven = NOT_GIVEN,
            inpainting_fill_res_padding: Optional[int] | NotGiven = NOT_GIVEN,
            inpainting_mask_invert: Optional[int] | NotGiven = NOT_GIVEN,
            initial_noise_multiplier: Optional[float] | NotGiven = NOT_GIVEN,
            latent_mask: Optional[str] | NotGiven = NOT_GIVEN,
            sampler_index: Optional[str] | NotGiven = NOT_GIVEN,
            include_init_images: Optional[bool] | NotGiven = NOT_GIVEN,
            script_name: Optional[str] | NotGiven = NOT_GIVEN,
            script_args: Optional[List[str]] | NotGiven = NOT_GIVEN,
            send_images: Optional[bool] | NotGiven = NOT_GIVEN,
            save_images: Optional[bool] | NotGiven = NOT_GIVEN,
            alwayson_scripts: Optional[Dict[str, Any]] | NotGiven = NOT_GIVEN,
            # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
            # The extra values given here take precedence over values defined on the client or passed to this method.
            extra_headers: Headers | None = None,
            extra_query: Query | None = None,
            extra_body: Body | None = None,
            timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ImagesResponse:
        """
        Creates an image given a prompt.

        Args:
          init_images:

          prompt: A text description of the desired image(s).

          negative_prompt:

          batch_size:

          steps:

          cfg_scale:

          width:

          height:

          seed:

          styles:

          subseed_enable_extras:

          denoising_strength:

          s_min_uncond:

          refiner_checkpoint:

          refiner_switch_at:

          disable_extra_networks:

          comments:

          resize_mode:

          image_cfg_scale:

          subseed:

          subseed_strength:

          seed_resize_from_h:

          seed_resize_from_w:

          sampler_name:

          restore_faces:

          tiling:

          do_not_save_samples:

          do_not_save_grid:

          eta:

          s_churn:

          s_tmax:

          s_tmin:

          s_noise:

          override_settings:

          override_settings_restore_afterwards:

          script_args:

          sampler_index:

          script_name:

          send_images:

          save_images:

          alwayson_scripts:

          nsfw:

          mask_blur_x:

          mask_blur_y:

          mask_blur:

          inpainting_fill:

          inpainting_fill_res:

          inpainting_fill_res_padding:

          inpainting_mask_invert:

          initial_noise_multiplier:

          latent_mask:

          include_init_images:

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        base64_images = []
        for file in init_images:
            base64_images.append(file_to_base64(file))
        body = deepcopy_minimal(
            {
                "init_images": base64_images,
                "prompt": prompt,
                "negative_prompt": negative_prompt,
                "batch_size": batch_size,
                "steps": steps,
                "cfg_scale": cfg_scale,
                "width": width,
                "height": height,
                "seed": seed,
                "styles": styles,
                "denoising_strength": denoising_strength,
                "subseed": subseed,
                "subseed_strength": subseed_strength,
                "seed_resize_from_h": seed_resize_from_h,
                "seed_resize_from_w": seed_resize_from_w,
                "sampler_name": sampler_name,
                "restore_faces": restore_faces,
                "tiling": tiling,
                "do_not_save_samples": do_not_save_samples,
                "do_not_save_grid": do_not_save_grid,
                "eta": eta,
                "s_churn": s_churn,
                "s_tmax": s_tmax,
                "s_tmin": s_tmin,
                "s_noise": s_noise,
                "override_settings": override_settings,
                "override_settings_restore_afterwards": override_settings_restore_afterwards,
                "script_args": script_args,
                "sampler_index": sampler_index,
                "script_name": script_name,
                "send_images": send_images,
                "save_images": save_images,
                "alwayson_scripts": alwayson_scripts,
                "subseed_enable_extras": subseed_enable_extras,
                "s_min_uncond": s_min_uncond,
                "refiner_checkpoint": refiner_checkpoint,
                "comments": comments,
                "refiner_switch_at": refiner_switch_at,
                "disable_extra_networks": disable_extra_networks,
                "resize_mode": resize_mode,
                "image_cfg_scale": image_cfg_scale,
                "mask_blur_x": mask_blur_x,
                "mask_blur_y": mask_blur_y,
                "mask_blur": mask_blur,
                "inpainting_fill": inpainting_fill,
                "inpainting_fill_res": inpainting_fill_res,
                "inpainting_fill_res_padding": inpainting_fill_res_padding,
                "inpainting_mask_invert": inpainting_mask_invert,
                "initial_noise_multiplier": initial_noise_multiplier,
                "latent_mask": latent_mask,
                "include_init_images": include_init_images
            }
        )
        return self._post(
            self._client.urls.url_img2img,
            body=maybe_transform(body, image_create_variation_params.ImageCreateVariationParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImagesResponse,
        )

    def generate(
            self,
            *,
            prompt: str,
            negative_prompt: Optional[str] | NotGiven = NOT_GIVEN,
            styles: Optional[List[str]] | NotGiven = NOT_GIVEN,
            seed: Optional[int] | NotGiven = NOT_GIVEN,
            subseed: Optional[int] | NotGiven = NOT_GIVEN,
            subseed_strength: Optional[float] | NotGiven = NOT_GIVEN,
            seed_resize_from_h: Optional[int] | NotGiven = NOT_GIVEN,
            seed_resize_from_w: Optional[int] | NotGiven = NOT_GIVEN,
            sampler_name: Optional[str] | NotGiven = NOT_GIVEN,
            batch_size: Optional[int] | NotGiven = NOT_GIVEN,
            n_iter: Optional[int] | NotGiven = NOT_GIVEN,
            steps: Optional[int] | NotGiven = NOT_GIVEN,
            cfg_scale: Optional[float] | NotGiven = NOT_GIVEN,
            width: Optional[int] | NotGiven = NOT_GIVEN,
            height: Optional[int] | NotGiven = NOT_GIVEN,
            restore_faces: Optional[bool] | NotGiven = NOT_GIVEN,
            tiling: Optional[bool] | NotGiven = NOT_GIVEN,
            do_not_save_samples: Optional[bool] | NotGiven = NOT_GIVEN,
            do_not_save_grid: Optional[bool] | NotGiven = NOT_GIVEN,
            eta: Optional[float] | NotGiven = NOT_GIVEN,
            denoising_strength: Optional[float] | NotGiven = NOT_GIVEN,
            s_min_uncond: Optional[float] | NotGiven = NOT_GIVEN,
            s_churn: Optional[float] | NotGiven = NOT_GIVEN,
            s_tmax: Optional[float] | NotGiven = NOT_GIVEN,
            s_tmin: Optional[float] | NotGiven = NOT_GIVEN,
            s_noise: Optional[float] | NotGiven = NOT_GIVEN,
            override_settings: Optional[Dict[str, Any]] | NotGiven = NOT_GIVEN,
            override_settings_restore_afterwards: Optional[bool] | NotGiven = NOT_GIVEN,
            refiner_checkpoint: Optional[str] | NotGiven = NOT_GIVEN,
            refiner_switch_at: Optional[float] | NotGiven = NOT_GIVEN,
            disable_extra_networks: Optional[bool] | NotGiven = NOT_GIVEN,
            comments: Optional[Dict[str, Any]] | NotGiven = NOT_GIVEN,
            enable_hr: Optional[bool] | NotGiven = NOT_GIVEN,
            firstphase_width: Optional[int] | NotGiven = NOT_GIVEN,
            firstphase_height: Optional[int] | NotGiven = NOT_GIVEN,
            hr_scale: Optional[float] | NotGiven = NOT_GIVEN,
            hr_upscaler: Optional[str] | NotGiven = NOT_GIVEN,
            hr_second_pass_steps: Optional[int] | NotGiven = NOT_GIVEN,
            hr_resize_x: Optional[int] | NotGiven = NOT_GIVEN,
            hr_resize_y: Optional[int] | NotGiven = NOT_GIVEN,
            hr_checkpoint_name: Optional[str] | NotGiven = NOT_GIVEN,
            hr_sampler_name: Optional[str] | NotGiven = NOT_GIVEN,
            hr_prompt: Optional[str] | NotGiven = NOT_GIVEN,
            hr_negative_prompt: Optional[str] | NotGiven = NOT_GIVEN,
            sampler_index: Optional[str] | NotGiven = NOT_GIVEN,
            script_name: Optional[str] | NotGiven = NOT_GIVEN,
            script_args: Optional[List[str]] | NotGiven = NOT_GIVEN,
            send_images: Optional[bool] | NotGiven = NOT_GIVEN,
            save_images: Optional[bool] | NotGiven = NOT_GIVEN,
            alwayson_scripts: Optional[Dict[str, Any]] | NotGiven = NOT_GIVEN,
            # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
            # The extra values given here take precedence over values defined on the client or passed to this method.
            extra_headers: Headers | None = None,
            extra_query: Query | None = None,
            extra_body: Body | None = None,
            timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ImagesResponse:
        """
        Creates an image given a prompt.

        Args:
          prompt: The input text that guides the model to generate an image according to the given textual description.

          negative_prompt:Textual guidance on what NOT to include in the generated image.

          batch_size:Number of images to generate in parallel.

          steps: Steps taken during the iterative generation process.

          cfg_scale:A scale factor for the model configuration.

          width:Output width of the generated image.

          height:Output height of the generated image.

          n_iter: Number of iterations the diffusion process will run for.

          seed: Seeds to control the generation process.

          styles:Artistic styles of generated image.

          enable_hr:Whether to enable high-resolution generation.

          denoising_strength: Parameters fine-tuning the denoising process.

          firstphase_width:

          firstphase_height:

          hr_scale: Upscaling factor for high-res generation if enabled.

          hr_upscaler: Name of the upscaling method.

          hr_second_pass_steps:Number of second pass steps for HR generation.

          s_min_uncond:Parameters fine-tuning the denoising process.

          hr_resize_x:

          hr_resize_y:

          subseed: Subseeds to control the generation process.

          disable_extra_networks:Whether to disable extra networks.

          comments:Placeholder for comments or metadata.

          refiner_checkpoint:Path to a checkpoint for an optional refining network.

          subseed_strength:How strongly to apply the subseed.

          seed_resize_from_h:Initial dimensions for resizing a potential seed image, if applicable.

          seed_resize_from_w:Initial dimensions for resizing a potential seed image, if applicable.

          sampler_name:Name of the sampling method to use.

          restore_faces:Whether to refine facial features.

          tiling:Whether to use tiled generation for high-resolution output.

          do_not_save_samples:Whether to save the individual samples.

          do_not_save_grid:Whether to save the individual  grid of samples.

          hr_checkpoint_name:

          hr_sampler_name:

          hr_prompt:

          eta:Parameters fine-tuning the denoising process.

          s_churn:Parameters fine-tuning the denoising process.

          s_tmax:Parameters fine-tuning the denoising process.

          s_tmin:Parameters fine-tuning the denoising process.

          s_noise:Parameters fine-tuning the denoising process.

          override_settings:Dictionary to override certain model settings.

          override_settings_restore_afterwards:Whether to restore original settings after applying overrides.

          script_args:Optional scripts to run along with generation.

          sampler_index:Type of sampler to use.

          script_name:Optional scripts to run along with generation.

          send_images:Flags indicating whether to send images back to the caller or save them locally.

          save_images:Flags indicating whether to send images back to the caller or save them locally.

          alwayson_scripts:Additional scripts that always run during generation.

          refiner_switch_at:At which step to switch to the refiner network.

          hr_negative_prompt:

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            self._client.urls.url_txt2img,
            body=maybe_transform(
                {
                    "prompt": prompt,
                    "negative_prompt": negative_prompt,
                    "batch_size": batch_size,
                    "steps": steps,
                    "cfg_scale": cfg_scale,
                    "n_iter": n_iter,
                    "width": width,
                    "height": height,
                    "seed": seed,
                    "styles": styles,
                    "enable_hr": enable_hr,
                    "denoising_strength": denoising_strength,
                    "firstphase_width": firstphase_width,
                    "firstphase_height": firstphase_height,
                    "s_min_uncond": s_min_uncond,
                    "hr_scale": hr_scale,
                    "hr_upscaler": hr_upscaler,
                    "hr_second_pass_steps": hr_second_pass_steps,
                    "hr_resize_x": hr_resize_x,
                    "hr_resize_y": hr_resize_y,
                    "subseed": subseed,
                    "subseed_strength": subseed_strength,
                    "seed_resize_from_h": seed_resize_from_h,
                    "seed_resize_from_w": seed_resize_from_w,
                    "sampler_name": sampler_name,
                    "restore_faces": restore_faces,
                    "tiling": tiling,
                    "do_not_save_samples": do_not_save_samples,
                    "do_not_save_grid": do_not_save_grid,
                    "eta": eta,
                    "s_churn": s_churn,
                    "s_tmax": s_tmax,
                    "s_tmin": s_tmin,
                    "s_noise": s_noise,
                    "override_settings": override_settings,
                    "override_settings_restore_afterwards": override_settings_restore_afterwards,
                    "script_args": script_args,
                    "sampler_index": sampler_index,
                    "script_name": script_name,
                    "send_images": send_images,
                    "save_images": save_images,
                    "alwayson_scripts": alwayson_scripts,
                    "refiner_checkpoint": refiner_checkpoint,
                    "refiner_switch_at": refiner_switch_at,
                    "hr_sampler_name": hr_sampler_name,
                    "hr_checkpoint_name": hr_checkpoint_name,
                    "hr_prompt": hr_prompt,
                    "hr_negative_prompt": hr_negative_prompt,
                    "disable_extra_networks": disable_extra_networks,
                    "comments": comments
                },
                image_generate_params.ImageGenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImagesResponse,
        )


class AsyncImages(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncImagesWithRawResponse:
        return AsyncImagesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncImagesWithStreamingResponse:
        return AsyncImagesWithStreamingResponse(self)

    async def generate(
            self,
            *,
            prompt: str,
            negative_prompt: Optional[str] | NotGiven = NOT_GIVEN,
            styles: Optional[List[str]] | NotGiven = NOT_GIVEN,
            seed: Optional[int] | NotGiven = NOT_GIVEN,
            subseed: Optional[int] | NotGiven = NOT_GIVEN,
            subseed_strength: Optional[float] | NotGiven = NOT_GIVEN,
            seed_resize_from_h: Optional[int] | NotGiven = NOT_GIVEN,
            seed_resize_from_w: Optional[int] | NotGiven = NOT_GIVEN,
            sampler_name: Optional[str] | NotGiven = NOT_GIVEN,
            batch_size: Optional[int] | NotGiven = NOT_GIVEN,
            n_iter: Optional[int] | NotGiven = NOT_GIVEN,
            steps: Optional[int] | NotGiven = NOT_GIVEN,
            cfg_scale: Optional[float] | NotGiven = NOT_GIVEN,
            width: Optional[int] | NotGiven = NOT_GIVEN,
            height: Optional[int] | NotGiven = NOT_GIVEN,
            restore_faces: Optional[bool] | NotGiven = NOT_GIVEN,
            tiling: Optional[bool] | NotGiven = NOT_GIVEN,
            do_not_save_samples: Optional[bool] | NotGiven = NOT_GIVEN,
            do_not_save_grid: Optional[bool] | NotGiven = NOT_GIVEN,
            eta: Optional[float] | NotGiven = NOT_GIVEN,
            denoising_strength: Optional[float] | NotGiven = NOT_GIVEN,
            s_min_uncond: Optional[float] | NotGiven = NOT_GIVEN,
            s_churn: Optional[float] | NotGiven = NOT_GIVEN,
            s_tmax: Optional[float] | NotGiven = NOT_GIVEN,
            s_tmin: Optional[float] | NotGiven = NOT_GIVEN,
            s_noise: Optional[float] | NotGiven = NOT_GIVEN,
            override_settings: Optional[Dict[str, Any]] | NotGiven = NOT_GIVEN,
            override_settings_restore_afterwards: Optional[bool] | NotGiven = NOT_GIVEN,
            refiner_checkpoint: Optional[str] | NotGiven = NOT_GIVEN,
            refiner_switch_at: Optional[float] | NotGiven = NOT_GIVEN,
            disable_extra_networks: Optional[bool] | NotGiven = NOT_GIVEN,
            comments: Optional[Dict[str, Any]] | NotGiven = NOT_GIVEN,
            enable_hr: Optional[bool] | NotGiven = NOT_GIVEN,
            firstphase_width: Optional[int] | NotGiven = NOT_GIVEN,
            firstphase_height: Optional[int] | NotGiven = NOT_GIVEN,
            hr_scale: Optional[float] | NotGiven = NOT_GIVEN,
            hr_upscaler: Optional[str] | NotGiven = NOT_GIVEN,
            hr_second_pass_steps: Optional[int] | NotGiven = NOT_GIVEN,
            hr_resize_x: Optional[int] | NotGiven = NOT_GIVEN,
            hr_resize_y: Optional[int] | NotGiven = NOT_GIVEN,
            hr_checkpoint_name: Optional[str] | NotGiven = NOT_GIVEN,
            hr_sampler_name: Optional[str] | NotGiven = NOT_GIVEN,
            hr_prompt: Optional[str] | NotGiven = NOT_GIVEN,
            hr_negative_prompt: Optional[str] | NotGiven = NOT_GIVEN,
            sampler_index: Optional[str] | NotGiven = NOT_GIVEN,
            script_name: Optional[str] | NotGiven = NOT_GIVEN,
            script_args: Optional[List[str]] | NotGiven = NOT_GIVEN,
            send_images: Optional[bool] | NotGiven = NOT_GIVEN,
            save_images: Optional[bool] | NotGiven = NOT_GIVEN,
            alwayson_scripts: Optional[Dict[str, Any]] | NotGiven = NOT_GIVEN,
            # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
            # The extra values given here take precedence over values defined on the client or passed to this method.
            extra_headers: Headers | None = None,
            extra_query: Query | None = None,
            extra_body: Body | None = None,
            timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ImagesResponse:
        """
        Creates an image given a prompt.

        Args:
          prompt: The input text that guides the model to generate an image according to the given textual description.

          negative_prompt:Textual guidance on what NOT to include in the generated image.

          batch_size:Number of images to generate in parallel.

          steps: Steps taken during the iterative generation process.

          cfg_scale:A scale factor for the model configuration.

          width:Output width of the generated image.

          height:Output height of the generated image.

          n_iter: Number of iterations the diffusion process will run for.

          seed: Seeds to control the generation process.

          styles:Artistic styles of generated image.

          enable_hr:Whether to enable high-resolution generation.

          denoising_strength: Parameters fine-tuning the denoising process.

          firstphase_width:

          firstphase_height:

          hr_scale: Upscaling factor for high-res generation if enabled.

          hr_upscaler: Name of the upscaling method.

          hr_second_pass_steps:Number of second pass steps for HR generation.

          s_min_uncond:Parameters fine-tuning the denoising process.

          hr_resize_x:

          hr_resize_y:

          subseed: Subseeds to control the generation process.

          disable_extra_networks:Whether to disable extra networks.

          comments:Placeholder for comments or metadata.

          refiner_checkpoint:Path to a checkpoint for an optional refining network.

          subseed_strength:How strongly to apply the subseed.

          seed_resize_from_h:Initial dimensions for resizing a potential seed image, if applicable.

          seed_resize_from_w:Initial dimensions for resizing a potential seed image, if applicable.

          sampler_name:Name of the sampling method to use.

          restore_faces:Whether to refine facial features.

          tiling:Whether to use tiled generation for high-resolution output.

          do_not_save_samples:Whether to save the individual samples.

          do_not_save_grid:Whether to save the individual  grid of samples.

          hr_checkpoint_name:

          hr_sampler_name:

          hr_prompt:

          eta:Parameters fine-tuning the denoising process.

          s_churn:Parameters fine-tuning the denoising process.

          s_tmax:Parameters fine-tuning the denoising process.

          s_tmin:Parameters fine-tuning the denoising process.

          s_noise:Parameters fine-tuning the denoising process.

          override_settings:Dictionary to override certain model settings.

          override_settings_restore_afterwards:Whether to restore original settings after applying overrides.

          script_args:Optional scripts to run along with generation.

          sampler_index:Type of sampler to use.

          script_name:Optional scripts to run along with generation.

          send_images:Flags indicating whether to send images back to the caller or save them locally.

          save_images:Flags indicating whether to send images back to the caller or save them locally.

          alwayson_scripts:Additional scripts that always run during generation.

          refiner_switch_at:At which step to switch to the refiner network.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            self._client.urls.url_txt2img,
            body=maybe_transform(
                {
                    "prompt": prompt,
                    "negative_prompt": negative_prompt,
                    "batch_size": batch_size,
                    "steps": steps,
                    "cfg_scale": cfg_scale,
                    "n_iter": n_iter,
                    "width": width,
                    "height": height,
                    "seed": seed,
                    "styles": styles,
                    "enable_hr": enable_hr,
                    "denoising_strength": denoising_strength,
                    "firstphase_width": firstphase_width,
                    "firstphase_height": firstphase_height,
                    "s_min_uncond": s_min_uncond,
                    "hr_scale": hr_scale,
                    "hr_upscaler": hr_upscaler,
                    "hr_second_pass_steps": hr_second_pass_steps,
                    "hr_resize_x": hr_resize_x,
                    "hr_resize_y": hr_resize_y,
                    "subseed": subseed,
                    "subseed_strength": subseed_strength,
                    "seed_resize_from_h": seed_resize_from_h,
                    "seed_resize_from_w": seed_resize_from_w,
                    "sampler_name": sampler_name,
                    "restore_faces": restore_faces,
                    "tiling": tiling,
                    "do_not_save_samples": do_not_save_samples,
                    "do_not_save_grid": do_not_save_grid,
                    "eta": eta,
                    "s_churn": s_churn,
                    "s_tmax": s_tmax,
                    "s_tmin": s_tmin,
                    "s_noise": s_noise,
                    "override_settings": override_settings,
                    "override_settings_restore_afterwards": override_settings_restore_afterwards,
                    "script_args": script_args,
                    "sampler_index": sampler_index,
                    "script_name": script_name,
                    "send_images": send_images,
                    "save_images": save_images,
                    "alwayson_scripts": alwayson_scripts,
                    "refiner_checkpoint": refiner_checkpoint,
                    "refiner_switch_at": refiner_switch_at,
                    "hr_sampler_name": hr_sampler_name,
                    "hr_checkpoint_name": hr_checkpoint_name,
                    "hr_prompt": hr_prompt,
                    "hr_negative_prompt": hr_negative_prompt,
                    "disable_extra_networks": disable_extra_networks,
                    "comments": comments
                },
                image_generate_params.ImageGenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImagesResponse,
        )

    async def create_variation(
            self,
            *,
            init_images: List[FileContent],
            prompt: Optional[str] | NotGiven = NOT_GIVEN,
            negative_prompt: Optional[str] | NotGiven = NOT_GIVEN,
            styles: Optional[List[str]] | NotGiven = NOT_GIVEN,
            seed: Optional[int] | NotGiven = NOT_GIVEN,
            subseed: Optional[int] | NotGiven = NOT_GIVEN,
            subseed_strength: Optional[float] | NotGiven = NOT_GIVEN,
            subseed_enable_extras: Optional[bool] | NotGiven = NOT_GIVEN,
            seed_resize_from_h: Optional[int] | NotGiven = NOT_GIVEN,
            seed_resize_from_w: Optional[int] | NotGiven = NOT_GIVEN,
            sampler_name: Optional[str] | NotGiven = NOT_GIVEN,
            batch_size: Optional[int] | NotGiven = NOT_GIVEN,
            steps: Optional[int] | NotGiven = NOT_GIVEN,
            cfg_scale: Optional[float] | NotGiven = NOT_GIVEN,
            width: Optional[int] | NotGiven = NOT_GIVEN,
            height: Optional[int] | NotGiven = NOT_GIVEN,
            restore_faces: Optional[bool] | NotGiven = NOT_GIVEN,
            tiling: Optional[bool] | NotGiven = NOT_GIVEN,
            do_not_save_samples: Optional[bool] | NotGiven = NOT_GIVEN,
            do_not_save_grid: Optional[bool] | NotGiven = NOT_GIVEN,
            eta: Optional[float] | NotGiven = NOT_GIVEN,
            denoising_strength: Optional[float] | NotGiven = NOT_GIVEN,
            s_min_uncond: Optional[float] | NotGiven = NOT_GIVEN,
            s_churn: Optional[float] | NotGiven = NOT_GIVEN,
            s_tmax: Optional[float] | NotGiven = NOT_GIVEN,
            s_tmin: Optional[float] | NotGiven = NOT_GIVEN,
            s_noise: Optional[float] | NotGiven = NOT_GIVEN,
            override_settings: Optional[Dict[str, Any]] | NotGiven = NOT_GIVEN,
            override_settings_restore_afterwards: Optional[bool] | NotGiven = NOT_GIVEN,
            refiner_checkpoint: Optional[bool] | NotGiven = NOT_GIVEN,
            refiner_switch_at: Optional[float] | NotGiven = NOT_GIVEN,
            disable_extra_networks: Optional[bool] | NotGiven = NOT_GIVEN,
            comments: Optional[Dict[str, Any]] | NotGiven = NOT_GIVEN,
            resize_mode: Optional[int] | NotGiven = NOT_GIVEN,
            image_cfg_scale: Optional[float] | NotGiven = NOT_GIVEN,
            mask_blur_x: Optional[int] | NotGiven = NOT_GIVEN,
            mask_blur_y: Optional[int] | NotGiven = NOT_GIVEN,
            mask_blur: Optional[int] | NotGiven = NOT_GIVEN,
            inpainting_fill: Optional[int] | NotGiven = NOT_GIVEN,
            inpainting_fill_res: Optional[int] | NotGiven = NOT_GIVEN,
            inpainting_fill_res_padding: Optional[int] | NotGiven = NOT_GIVEN,
            inpainting_mask_invert: Optional[int] | NotGiven = NOT_GIVEN,
            initial_noise_multiplier: Optional[float] | NotGiven = NOT_GIVEN,
            latent_mask: Optional[str] | NotGiven = NOT_GIVEN,
            sampler_index: Optional[str] | NotGiven = NOT_GIVEN,
            include_init_images: Optional[bool] | NotGiven = NOT_GIVEN,
            script_name: Optional[str] | NotGiven = NOT_GIVEN,
            script_args: Optional[List[str]] | NotGiven = NOT_GIVEN,
            send_images: Optional[bool] | NotGiven = NOT_GIVEN,
            save_images: Optional[bool] | NotGiven = NOT_GIVEN,
            alwayson_scripts: Optional[Dict[str, Any]] | NotGiven = NOT_GIVEN,
            # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
            # The extra values given here take precedence over values defined on the client or passed to this method.
            extra_headers: Headers | None = None,
            extra_query: Query | None = None,
            extra_body: Body | None = None,
            timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ImagesResponse:
        """
        Creates an image given a prompt.

        Args:
          init_images:

          prompt: A text description of the desired image(s).

          negative_prompt:

          batch_size:

          steps:

          cfg_scale:

          width:

          height:

          seed:

          styles:

          subseed_enable_extras:

          denoising_strength:

          s_min_uncond:

          refiner_checkpoint:

          refiner_switch_at:

          disable_extra_networks:

          comments:

          resize_mode:

          image_cfg_scale:

          subseed:

          subseed_strength:

          seed_resize_from_h:

          seed_resize_from_w:

          sampler_name:

          restore_faces:

          tiling:

          do_not_save_samples:

          do_not_save_grid:

          eta:

          s_churn:

          s_tmax:

          s_tmin:

          s_noise:

          override_settings:

          override_settings_restore_afterwards:

          script_args:

          sampler_index:

          script_name:

          send_images:

          save_images:

          alwayson_scripts:

          nsfw:

          mask_blur_x:

          mask_blur_y:

          mask_blur:

          inpainting_fill:

          inpainting_fill_res:

          inpainting_fill_res_padding:

          inpainting_mask_invert:

          initial_noise_multiplier:

          latent_mask:

          include_init_images:

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        base64_images = []
        for file in init_images:
            base64_images.append(file_to_base64(file))
        body = deepcopy_minimal(
            {
                "init_images": base64_images,
                "prompt": prompt,
                "negative_prompt": negative_prompt,
                "batch_size": batch_size,
                "steps": steps,
                "cfg_scale": cfg_scale,
                "width": width,
                "height": height,
                "seed": seed,
                "styles": styles,
                "denoising_strength": denoising_strength,
                "subseed": subseed,
                "subseed_strength": subseed_strength,
                "seed_resize_from_h": seed_resize_from_h,
                "seed_resize_from_w": seed_resize_from_w,
                "sampler_name": sampler_name,
                "restore_faces": restore_faces,
                "tiling": tiling,
                "do_not_save_samples": do_not_save_samples,
                "do_not_save_grid": do_not_save_grid,
                "eta": eta,
                "s_churn": s_churn,
                "s_tmax": s_tmax,
                "s_tmin": s_tmin,
                "s_noise": s_noise,
                "override_settings": override_settings,
                "override_settings_restore_afterwards": override_settings_restore_afterwards,
                "script_args": script_args,
                "sampler_index": sampler_index,
                "script_name": script_name,
                "send_images": send_images,
                "save_images": save_images,
                "alwayson_scripts": alwayson_scripts,
                "subseed_enable_extras": subseed_enable_extras,
                "s_min_uncond": s_min_uncond,
                "refiner_checkpoint": refiner_checkpoint,
                "comments": comments,
                "refiner_switch_at": refiner_switch_at,
                "disable_extra_networks": disable_extra_networks,
                "resize_mode": resize_mode,
                "image_cfg_scale": image_cfg_scale,
                "mask_blur_x": mask_blur_x,
                "mask_blur_y": mask_blur_y,
                "mask_blur": mask_blur,
                "inpainting_fill": inpainting_fill,
                "inpainting_fill_res": inpainting_fill_res,
                "inpainting_fill_res_padding": inpainting_fill_res_padding,
                "inpainting_mask_invert": inpainting_mask_invert,
                "initial_noise_multiplier": initial_noise_multiplier,
                "latent_mask": latent_mask,
                "include_init_images": include_init_images
            }
        )
        return await self._post(
            self._client.urls.url_img2img,
            body=maybe_transform(body, image_create_variation_params.ImageCreateVariationParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImagesResponse,
        )


class ImagesWithRawResponse:
    def __init__(self, images: Images) -> None:
        self._images = images

        self.generate = _legacy_response.to_raw_response_wrapper(
            images.generate,
        )


class AsyncImagesWithRawResponse:
    def __init__(self, images: AsyncImages) -> None:
        self._images = images

        self.generate = _legacy_response.async_to_raw_response_wrapper(
            images.generate,
        )


class ImagesWithStreamingResponse:
    def __init__(self, images: Images) -> None:
        self._images = images

        self.generate = to_streamed_response_wrapper(
            images.generate,
        )


class AsyncImagesWithStreamingResponse:
    def __init__(self, images: AsyncImages) -> None:
        self._images = images

        self.generate = async_to_streamed_response_wrapper(
            images.generate,
        )
