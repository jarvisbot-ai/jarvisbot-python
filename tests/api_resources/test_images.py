from __future__ import annotations

import pytest

from jarvisbot import JarvisBot, AsyncJarvisBot
from jarvisbot.types import ImagesResponse
from tests.utils import assert_matches_type


class TestImages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_generate(self, client: JarvisBot) -> None:
        image = client.base.images.generate(
            prompt="A cute baby sea otter",
        )
        assert_matches_type(ImagesResponse, image, path=["response"])

    @parametrize
    def test_method_generate_with_all_params(self, client: JarvisBot) -> None:
        image = client.base.images.generate(
            prompt="A cute baby sea otter",
            negative_prompt="deformed iris",
            styles=[],
            seed=-1,
            subseed=-1,
            subseed_strength=0,
            seed_resize_from_h=-1,
            seed_resize_from_w=-1,
            sampler_name="",
            batch_size=1,
            n_iter=1,
            steps=20,
            cfg_scale=6,
            width=512,
            height=768,
            restore_faces=False,
            tiling=False,
            do_not_save_samples=False,
            do_not_save_grid=False,
            eta=0,
            denoising_strength=0,
            s_min_uncond=0,
            s_churn=0,
            s_tmax=0,
            s_tmin=0,
            s_noise=1,
            override_settings={"sd_model_checkpoint": "photon_v1.safetensors"},
            override_settings_restore_afterwards=False,
            refiner_checkpoint="",
            refiner_switch_at=0,
            disable_extra_networks=False,
            comments={},
            enable_hr=False,
            firstphase_width=0,
            firstphase_height=0,
            hr_scale=2,
            hr_upscaler="",
            hr_second_pass_steps=0,
            hr_resize_x=0,
            hr_resize_y=0,
            hr_checkpoint_name="string",
            hr_sampler_name="string",
            hr_prompt="",
            hr_negative_prompt="",
            sampler_index="Euler",
            script_name="",
            script_args=[],
            send_images=True,
            save_images=False,
            alwayson_scripts={},
        )
        assert_matches_type(ImagesResponse, image, path=["response"])


class TestAsyncImages:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_generate(self, async_client: AsyncJarvisBot) -> None:
        image = await async_client.base.images.generate(
            prompt="A cute baby sea otter",
        )
        assert_matches_type(ImagesResponse, image, path=["response"])

    @parametrize
    async def test_method_generate_with_all_params(self, async_client: AsyncJarvisBot) -> None:
        image = await async_client.base.images.generate(
            prompt="A cute baby sea otter",
            negative_prompt="deformed iris",
            styles=[],
            seed=-1,
            subseed=-1,
            subseed_strength=0,
            seed_resize_from_h=-1,
            seed_resize_from_w=-1,
            sampler_name="",
            batch_size=1,
            n_iter=1,
            steps=20,
            cfg_scale=6,
            width=512,
            height=768,
            restore_faces=False,
            tiling=False,
            do_not_save_samples=False,
            do_not_save_grid=False,
            eta=0,
            denoising_strength=0,
            s_min_uncond=0,
            s_churn=0,
            s_tmax=0,
            s_tmin=0,
            s_noise=1,
            override_settings={"sd_model_checkpoint": "photon_v1.safetensors"},
            override_settings_restore_afterwards=False,
            refiner_checkpoint="",
            refiner_switch_at=0,
            disable_extra_networks=False,
            comments={},
            enable_hr=False,
            firstphase_width=0,
            firstphase_height=0,
            hr_scale=2,
            hr_upscaler="",
            hr_second_pass_steps=0,
            hr_resize_x=0,
            hr_resize_y=0,
            hr_checkpoint_name="string",
            hr_sampler_name="string",
            hr_prompt="",
            hr_negative_prompt="",
            sampler_index="Euler",
            script_name="",
            script_args=[],
            send_images=True,
            save_images=False,
            alwayson_scripts={},
        )
        assert_matches_type(ImagesResponse, image, path=["response"])
