```bash
UNITER 首先使用 Image Embedder 和 Text Embedder 将图像区域（视觉特征和边界框特征）和文本词（标记和位置）编码到一个公共嵌入空间中，然后应用一个 Transformer 模块，通过上述预训练任务为每个区域和单词来学习可泛化的上下文。与使用两个流的 LXMERT和 ViLBERT 相比，UNITER 模型可以通过单个 Transformer 学习图像区域和文本词的联合上下文化表示。此外，作者的掩码语言/区域建模是基于对于图像/文本的全面观察，这与将联合随机掩码应用于两种模态的其他并行预训练模型不同。作者表明条件掩码策略可以成功地缓解图像和文本之间的缺失对齐，并为下游任务获得更好的联合嵌入。
```
```bash
给定一对图像和句子，UNITER 将图像的视觉区域和句子的文本标记作为输入。作者设计了一个图像嵌入器和一个文本嵌入器来提取它们各自的嵌入。然后将这些嵌入输入到多层 self-attention Transformer 中，用以学习视觉区域和文本标记之间的跨模态上下文嵌入。Transformer 中的 self-attention 机制是无序的，因此需要将标记/区域的位置/位置显式编码为附加输入。
```
```bash
具体来说，在 Image Embedder 中，作者首先使用 Faster R-CNN 来提取每个区域的视觉特征。此外作者还通过一个 7 维向量对每个区域的位置特征进行编码。然后，视觉和位置特征都通过一个全连接 (FC) 层，用以投影到相同的嵌入空间中。每个区域的最终视觉嵌入是通过将两个 FC 输出相加，然后通过层归一化 (LN) 层来得到的。对于Text Embedder，作者将输入句子标记为 WordPieces。每个子词标记的最终表示是通过总结其词嵌入和位置嵌入获得的，然后接着是另一个 LN 层。

作者用了三种任务预训练模型：基于图像的MLM，基于文本的MRM和图像文本匹配（ITM）。如图 1 所示，作者的 MRM 和 MLM 类似于 BERT，其中从输入中随机屏蔽一些单词或区域，Transformer 的输出是学习恢复这些单词或区域 。具体来说，词掩码是通过用特殊的标记 [MASK] 替换标记来实现的，区域掩码是通过将视觉特征向量替换为全零来实现的。

需要注意的是作者每次只屏蔽一种模态，同时保持另一种模态完好无损，而不是像 ViLBERT 和 LXMERT 那样随机屏蔽两种模态。当一个被屏蔽的区域碰巧被一个屏蔽词描述时，这可以防止潜在的未对齐。作者表示通过条件屏蔽，他们的模型能够学习更好的嵌入。最后，作者还通过 ITM 学习了整个图像和句子之间的实例级对齐（而不是标记/区域级）。在训练期间，作者对正负图像句子对进行采样，并学习它们的匹配分数。

为了使用上述不同任务对 UNITER 进行预训练，作者为每个小批量随机采样一个预训练任务，并且每次 SGD 更新仅对一个目标进行训练。
```