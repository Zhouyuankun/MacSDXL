# 如何使用stable diffusion在Apple Silicon芯片的Mac上画图（GPU加速）

## 下载需要的模型

下载模型：*stabilityai/stable-diffusion-xl-base-1.0*，使用[异形岛](https://aliendao.cn/#/)网站里的model_download.py文件下载


下载LCM-LoRA：*latent-consistency/lcm-lora-sdxl*，在[Hugging Face](https://huggingface.co/latent-consistency/lcm-lora-sdxl)下载该模型


## 创建python环境

在conda arm64环境下安装torch，transformers, diffusers等库

[PyTorch安装页面](https://pytorch.org/get-started/locally/)，使用命令：
`conda install pytorch::pytorch torchvision torchaudio -c pytorch`

[Transformers安装界面](https://huggingface.co/docs/transformers/installation#install-with-conda)，使用命令
`conda install -c huggingface transformers`

[Diffusers安装界面](https://huggingface.co/docs/diffusers/installation#install-with-conda)，使用命令
`conda install -c conda-forge diffusers`

## 运行程序

## 教程
[哔哩哔哩网站](https://www.bilibili.com/video/BV1G64y177EY/?spm_id_from=333.999.0.0)上有详细的操作流程，如有疑问可以观看视频讲解