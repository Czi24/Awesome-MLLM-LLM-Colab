# LLM101n: Let's build a Storyteller

![LLM101n header image](llm101n.jpg)

> What I cannot create, I do not understand. -Richard Feynman  
> 我不能创造的东西，我就无法理解。- 理查德·费曼

In this course we will build a Storyteller AI Large Language Model (LLM). Hand in hand, you'll be able create, refine and illustrate little [stories](https://huggingface.co/datasets/roneneldan/TinyStories) with the AI. We are going to build everything end-to-end from basics to a functioning web app similar to ChatGPT, from scratch in Python, C and CUDA, and with minimal computer science prerequisits. By the end you should have a relatively deep understanding of AI, LLMs, and deep learning more generally.  
在本课程中，我们将构建一个讲故事的AI大型语言模型（LLM）。通过合作，你将能够与AI一起创建、完善和展示小[故事](https://huggingface.co/datasets/roneneldan/TinyStories)。我们将从基础开始，端到端地构建一切，从头开始使用Python、C和CUDA，并且仅需最少的计算机科学先决条件。到最后，你应该对AI、LLM和深度学习有一个相对深入的理解。

**Syllabus**  
**课程大纲**

- [Chapter 01](https://github.com/karpathy/LLM101n/tree/master/bigram/README.md) **Bigram Language Model** (language modeling)  
  [第一章](https://github.com/Czi24/Awesome-MLLM-LLM-Colab/blob/master/LLM101n-Colab/bigram/README.md) **双字母语言模型**（语言建模）
- [Chapter 02](https://github.com/karpathy/LLM101n/tree/master/micrograd/README.md) **Micrograd** (machine learning, backpropagation)  
  [第二章](https://github.com/Czi24/Awesome-MLLM-LLM-Colab/blob/master/LLM101n-Colab/micrograd/README.md) **Micrograd**（机器学习，反向传播）
- [Chapter 03](https://github.com/karpathy/LLM101n/tree/master/mlp/README.md) **N-gram model** (multi-layer perceptron, matmul, gelu)  
  [第三章](https://github.com/Czi24/Awesome-MLLM-LLM-Colab/blob/master/LLM101n-Colab/mlp/README.md) **N元模型**（多层感知器，矩阵乘法，GELU）
- [Chapter 04](https://github.com/karpathy/LLM101n/tree/master/attention/README.md) **Attention** (attention, softmax, positional encoder)  
  [第四章](https://github.com/Czi24/Awesome-MLLM-LLM-Colab/blob/master/LLM101n-Colab/attention/README.md) **注意力机制**（注意力机制，softmax，位置编码器）
- [Chapter 05](https://github.com/karpathy/LLM101n/tree/master/transformer/README.md) **Transformer** (transformer, residual, layernorm, GPT-2)  
  [第五章](https://github.com/Czi24/Awesome-MLLM-LLM-Colab/blob/master/LLM101n-Colab/transformer/README.md) **Transformer**（transformer，残差，层归一化，GPT-2）
- [Chapter 06](https://github.com/karpathy/LLM101n/tree/master/tokenization/README.md) **Tokenization** (minBPE, byte pair encoding)  
  [第六章](https://github.com/Czi24/Awesome-MLLM-LLM-Colab/blob/master/LLM101n-Colab/tokenization/README.md) **分词**（minBPE，字节对编码）
- [Chapter 07](https://github.com/karpathy/LLM101n/tree/master/optimization/README.md) **Optimization** (initialization, optimization, AdamW)  
  [第七章](https://github.com/Czi24/Awesome-MLLM-LLM-Colab/blob/master/LLM101n-Colab/optimization/README.md) **优化**（初始化，优化，AdamW）
- [Chapter 08](https://github.com/karpathy/LLM101n/tree/master/device/README.md) **Need for Speed I: Device** (device, CPU, GPU, ...)  
  [第八章](https://github.com/Czi24/Awesome-MLLM-LLM-Colab/blob/master/LLM101n-Colab/device/README.md) **速度需求 I：设备**（设备，CPU，GPU，...）
- [Chapter 09](https://github.com/karpathy/LLM101n/tree/master/precision/README.md) **Need for Speed II: Precision** (mixed precision training, fp16, bf16, fp8, ...)  
  [第九章](https://github.com/Czi24/Awesome-MLLM-LLM-Colab/blob/master/LLM101n-Colab/precision/README.md) **速度需求 II：精度**（混合精度训练，fp16，bf16，fp8，...）
- [Chapter 10](https://github.com/karpathy/LLM101n/tree/master/distributed/README.md) **Need for Speed III: Distributed** (distributed optimization, DDP, ZeRO)  
  [第十章](https://github.com/Czi24/Awesome-MLLM-LLM-Colab/blob/master/LLM101n-Colab/distributed/README.md) **速度需求 III：分布式**（分布式优化，DDP，ZeRO）
- [Chapter 11](https://github.com/karpathy/LLM101n/tree/master/datasets/README.md) **Datasets** (datasets, data loading, synthetic data generation)  
  [第十一章](https://github.com/Czi24/Awesome-MLLM-LLM-Colab/blob/master/LLM101n-Colab/datasets/README.md) **数据集**（数据集，数据加载，合成数据生成）
- [Chapter 12](https://github.com/karpathy/LLM101n/tree/master/inference/README.md) **Inference I: kv-cache** (kv-cache)  
  [第十二章](https://github.com/Czi24/Awesome-MLLM-LLM-Colab/blob/master/LLM101n-Colab/inference/README.md) **推理 I：kv缓存**（kv缓存）
- [Chapter 13](https://github.com/karpathy/LLM101n/tree/master/quantization/README.md) **Inference II: Quantization** (quantization)  
  [第十三章](https://github.com/Czi24/Awesome-MLLM-LLM-Colab/blob/master/LLM101n-Colab/quantization/README.md) **推理 II：量化**（量化）
- [Chapter 14](https://github.com/karpathy/LLM101n/tree/master/sft/README.md) **Finetuning I: SFT** (supervised finetuning SFT, PEFT, LoRA, chat)  
  [第十四章](https://github.com/Czi24/Awesome-MLLM-LLM-Colab/blob/master/LLM101n-Colab/sft/README.md) **微调 I：SFT**（监督微调SFT，PEFT，LoRA，聊天）
- [Chapter 15](https://github.com/karpathy/LLM101n/tree/master/rl/README.md) **Finetuning II: RL** (reinforcement learning, RLHF, PPO, DPO)  
  [第十五章](https://github.com/Czi24/Awesome-MLLM-LLM-Colab/blob/master/LLM101n-Colab/rl/README.md) **微调 II：RL**（强化学习，RLHF，PPO，DPO）
- [Chapter 16](https://github.com/karpathy/LLM101n/tree/master/deployment/README.md) **Deployment** (API, web app)  
  [第十六章](https://github.com/Czi24/Awesome-MLLM-LLM-Colab/blob/master/LLM101n-Colab/deployment/README.md) **部署**（API，web应用）
- [Chapter 17](https://github.com/karpathy/LLM101n/tree/master/multimodal/README.md) **Multimodal** (VQVAE, diffusion transformer)  
  [第十七章](https://github.com/Czi24/Awesome-MLLM-LLM-Colab/blob/master/LLM101n-Colab/multimodal/README.md) **多模态**（VQVAE，扩散transformer）

**Appendix**  
**附录**

Further topics to work into the progression above:  
进一步融入上述课程的主题：

- Programming languages: Assembly, C, Python  
  编程语言：汇编，C，Python
- Data types: Integer, Float, String (ASCII, Unicode, UTF-8)  
  数据类型：整数，浮点数，字符串（ASCII，Unicode，UTF-8）
- Tensor: shapes, views, strides, contiguous, ...  
  张量：形状，视图，步幅，连续，...
- Deep Learning frameowrks: PyTorch, JAX  
  深度学习框架：PyTorch，JAX
- Neural Net Architecture: GPT (1,2,3,4), Llama (RoPE, RMSNorm, GQA), MoE, ...  
  神经网络架构：GPT（1,2,3,4），Llama（RoPE，RMSNorm，GQA），MoE，...
- Multimodal: Images, Audio, Video, VQVAE, VQGAN, diffusion  
  多模态：图像，音频，视频，VQVAE，VQGAN，扩散

---
