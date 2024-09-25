
# 构建一个大型语言模型（从零开始）

此仓库包含开发、预训练和微调一个类似GPT的大型语言模型（LLM）的代码，是书籍 [《从零开始构建大型语言模型》](http://mng.bz/orYv) 的官方代码仓库。

<br>
<br>

<a href="http://mng.bz/orYv"><img src="https://sebastianraschka.com/images/LLMs-from-scratch-images/cover.jpg?123" width="250px"></a>

<br>

在[*从零开始构建大型语言模型*](http://mng.bz/orYv)中，你将从内到外地了解大型语言模型（LLM）是如何工作的，并通过一步一步编写代码来构建它们。在这本书中，我将通过清晰的文本、图表和示例引导你创建自己的LLM，解释每个阶段的工作原理。

书中描述的训练和开发小型但功能齐全模型的方法，旨在为教育目的服务，其过程与创建类似于ChatGPT背后的大规模基础模型的过程类似。此外，这本书还包括加载更大预训练模型权重进行微调的代码。

- 官方 [源码仓库链接](https://github.com/rasbt/LLMs-from-scratch)
- [Manning书籍链接](http://mng.bz/orYv)
- [Amazon书籍页面链接](https://www.amazon.com/gp/product/1633437167)
- ISBN 9781633437166

<a href="http://mng.bz/orYv#reviews"><img src="https://sebastianraschka.com//images/LLMs-from-scratch-images/other/reviews.png" width="220px"></a>


<br>
<br>

要下载此仓库的副本，请点击 [Download ZIP](https://github.com/rasbt/LLMs-from-scratch/archive/refs/heads/main.zip) 按钮，或在终端中执行以下命令：

```bash
git clone --depth 1 https://github.com/rasbt/LLMs-from-scratch.git
```

<br>

（如果你从Manning网站下载了代码包，请访问GitHub上的官方代码仓库 [https://github.com/rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) 获取最新更新。）

<br>
<br>


# 目录

请注意，此 `README.md` 文件是一个Markdown（`.md`）文件。如果你从Manning网站下载了此代码包并在本地计算机上查看它，我建议使用Markdown编辑器或预览器来正确查看。如果你还没有安装Markdown编辑器，[MarkText](https://www.marktext.cc) 是一个不错的免费选项。

你也可以在浏览器中查看GitHub上的此文件和其他文件，地址是 [https://github.com/rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch)，GitHub会自动渲染Markdown。

<br>
<br>
<!--  -->

> [!提示]
> 如果你需要有关安装Python和Python包以及设置代码环境的指南，我建议阅读位于 [setup](setup) 目录中的 [README.md](setup/README.md) 文件。

<br>
<br>

[![代码测试（Linux）](https://github.com/rasbt/LLMs-from-scratch/actions/workflows/basic-tests-linux.yml/badge.svg)](https://github.com/rasbt/LLMs-from-scratch/actions/workflows/basic-tests-linux.yml)
[![代码测试（Windows）](https://github.com/rasbt/LLMs-from-scratch/actions/workflows/basic-tests-windows.yml/badge.svg)](https://github.com/rasbt/LLMs-from-scratch/actions/workflows/basic-tests-windows.yml)
[![代码测试（macOS）](https://github.com/rasbt/LLMs-from-scratch/actions/workflows/basic-tests-macos.yml/badge.svg)](https://github.com/rasbt/LLMs-from-scratch/actions/workflows/basic-tests-macos.yml)



<br>

| 章节标题                                                   | 主要代码（快速访问）                                                                                                             | 所有代码 + 补充材料           |
|------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| [设置建议](setup)                                           | -                                                                                                                               | -                             |
| 第1章：理解大型语言模型                                    | 无代码                                                                                                                          | -                             |
| 第2章：处理文本数据                                        | - [ch02.ipynb](ch02/01_main-chapter-code/ch02.ipynb)<br/>- [dataloader.ipynb](ch02/01_main-chapter-code/dataloader.ipynb)（摘要）<br/>- [exercise-solutions.ipynb](ch02/01_main-chapter-code/exercise-solutions.ipynb) | [./ch02](./ch02)              |
| 第3章：编码Attention机制                                   | - [ch03.ipynb](ch03/01_main-chapter-code/ch03.ipynb)<br/>- [multihead-attention.ipynb](ch03/01_main-chapter-code/multihead-attention.ipynb)（摘要） <br/>- [exercise-solutions.ipynb](ch03/01_main-chapter-code/exercise-solutions.ipynb) | [./ch03](./ch03)              |
| 第4章：从零实现GPT模型                                     | - [ch04.ipynb](ch04/01_main-chapter-code/ch04.ipynb)<br/>- [gpt.py](ch04/01_main-chapter-code/gpt.py)（摘要）<br/>- [exercise-solutions.ipynb](ch04/01_main-chapter-code/exercise-solutions.ipynb) | [./ch04](./ch04)              |
| 第5章：在未标记数据上进行预训练                            | - [ch05.ipynb](ch05/01_main-chapter-code/ch05.ipynb)<br/>- [gpt_train.py](ch05/01_main-chapter-code/gpt_train.py)（摘要）<br/>- [gpt_generate.py](ch05/01_main-chapter-code/gpt_generate.py)（摘要）<br/>- [exercise-solutions.ipynb](ch05/01_main-chapter-code/exercise-solutions.ipynb) | [./ch05](./ch05)              |
| 第6章：用于文本分类的微调                                  | - [ch06.ipynb](ch06/01_main-chapter-code/ch06.ipynb)  <br/>- [gpt_class_finetune.py](ch06/01_main-chapter-code/gpt_class_finetune.py)  <br/>- [exercise-solutions.ipynb](ch06/01_main-chapter-code/exercise-solutions.ipynb) | [./ch06](./ch06)              |
| 第7章：为指令执行进行微调                                  | - [ch07.ipynb](ch07/01_main-chapter-code/ch07.ipynb)<br/>- [gpt_instruction_finetuning.py](ch07/01_main-chapter-code/gpt_instruction_finetuning.py)（摘要）<br/>- [ollama_evaluate.py](ch07/01_main-chapter-code/ollama_evaluate.py)（摘要）<br/>- [exercise-solutions.ipynb](ch07/01_main-chapter-code/exercise-solutions.ipynb) | [./ch07](./ch07)              |
| 附录A：PyTorch简介                                         | - [code-part1.ipynb](appendix-A/01_main-chapter-code/code-part1.ipynb)<br/>- [code-part2.ipynb](appendix-A/01_main-chapter-code/code-part2.ipynb)<br/>- [DDP-script.py](appendix-A/01_main-chapter-code/DDP-script.py)<br/>- [exercise-solutions.ipynb](appendix-A/01_main-chapter-code/exercise-solutions.ipynb) | [./appendix-A](./appendix-A)   |
| 附录B：参考资料与延伸阅读                                  | 无代码                                                                                                                          | -                             |
| 附录C：练习解答                                             | 无代码                                                                                                                          | -                             |
| 附录D：为训练循环增加额外功能                               | - [appendix-D.ipynb](appendix-D/01_main-chapter-code/appendix-D.ipynb)                                                          | [./appendix-D](./appendix-D)   |
| 附录E：使用LoRA进行参数高效微调                            | - [appendix-E.ipynb](appendix-E/01_main-chapter-code/appendix-E.ipynb)                                                          | [./appendix-E](./appendix-E)   |

<br>
&nbsp;

下图总结了本书所涵盖的内容。

<img src="https://sebastianraschka.com/images/LLMs-from-scratch-images/mental-model.jpg" width="650px">

<br>
&nbsp;

## 硬件要求

本书主要章节中的代码设计为可以在普通笔记本电脑上以合理的时间范围内运行，不需要特殊的硬件。这种方法确保了广泛的受众能够参与其中。此外，代码会在检测到GPU时自动使用它们。（请参阅 [setup](https://github.com/rasbt/LLMs-from-scratch/blob/main/setup/README.md) 文档以获取额外建议。）

&nbsp;
## 额外材料

多个文件夹包含了一些可选材料，作为对感兴趣读者的额外奖励：

- **设置**
  - [Python 设置建议](setup/01_optional-python-setup-preferences)
  - [安装本书中使用的Python包和库](setup/02_installing-python-libraries)
  - [Docker环境设置指南](setup/03_optional-docker-environment)
- **第2章：**
  - [比较不同的Byte Pair Encoding (BPE)实现](ch02/02_bonus_bytepair-encoder)
  - [理解Embedding层和线性层的区别](ch02/03_bonus_embedding-vs-matmul)
  - [使用简单数字理解Dataloader](ch02/04_bonus_dataloader-intuition)
- **第3章：**
  - [比较高效的多头Attention实现](ch03/02_bonus_efficient-multihead-attention/mha-implementations.ipynb)
  - [理解PyTorch Buffers](ch03/03_understanding-buffers/understanding-buffers.ipynb)
- **第4章：**
  - [FLOPS分析](ch04/02_performance-analysis/flops-analysis.ipynb)
- **第5章：**
  - [从Hugging Face Model Hub加载权重的替代方案](ch05/02_alternative_weight_loading/weight-loading-hf-transformers.ipynb)
  - [在古登堡项目数据集上预训练GPT](ch05/03_bonus_pretraining_on_gutenberg)
  - [为训练循环添加额外功能](ch05/04_learning_rate_schedulers)
  - [预训练的超参数优化](ch05/05_bonus_hparam_tuning)
  - [构建与预训练LLM交互的用户界面](ch05/06_user_interface)
  - [将GPT转换为Llama](ch05/07_gpt_to_llama)
- **第6章：**
  - [微调不同层并使用更大模型的额外实验](ch06/02_bonus_additional-experiments)
  - [在50k IMDB电影评论数据集上微调不同的模型](ch06/03_bonus_imdb-classification)
  - [构建与基于GPT的垃圾邮件分类器交互的用户界面](ch06/04_user_interface)
- **第7章：**
  - [用于查找相似数据和创建被动语态条目的数据集工具](ch07/02_dataset-utilities)
  - [使用OpenAI API和Ollama评估指令响应](ch07/03_model-evaluation)
  - [生成用于指令微调的数据集](ch07/05_dataset-generation/llama3-ollama.ipynb)
  - [改进用于指令微调的数据集](ch07/05_dataset-generation/reflection-gpt4.ipynb)
  - [使用Llama 3.1 70B和Ollama生成偏好数据集](ch07/04_preference-tuning-with-dpo/create-preference-data-ollama.ipynb)
  - [用于LLM对齐的直接偏好优化 (DPO)](ch07/04_preference-tuning-with-dpo/dpo-from-scratch.ipynb)
  - [构建与指令微调GPT模型交互的用户界面](ch07/06_user_interface)

<br>
&nbsp;

## 问题、反馈与对本仓库的贡献


我欢迎各种反馈，最佳的反馈渠道是通过 [Manning论坛](https://livebook.manning.com/forum?product=raschka&page=1) 或 [GitHub Discussions](https://github.com/rasbt/LLMs-from-scratch/discussions)。同样，如果你有任何问题或只是想与其他人交流想法，也请不要犹豫，尽管在论坛中发布。

请注意，由于此仓库包含与印刷书籍对应的代码，目前我不能接受会扩展主要章节代码内容的贡献，因为这会导致与实体书内容的不一致。保持一致有助于确保所有人的顺畅体验。


&nbsp;
## 引用

如果你发现这本书或代码对你的研究有帮助，请考虑引用它。

芝加哥风格引用：

> Raschka, Sebastian. *Build A Large Language Model (From Scratch)*. Manning, 2024. ISBN: 978-1633437166.

BibTeX格式：

```
@book{build-llms-from-scratch-book,
  author       = {Sebastian Raschka},
  title        = {Build A Large Language Model (From Scratch)},
  publisher    = {Manning},
  year         = {2024},
  isbn         = {978-1633437166},
  url          = {https://www.manning.com/books/build-a-large-language-model-from-scratch},
  github       = {https://github.com/rasbt/LLMs-from-scratch}
}
```


