## Teacher Forcing

RNN을 사용하는 NLP 모델에서 RNN 셀들이 모두 값을 잘 예측하면 괜찮지만

어떤 셀이 예측을 잘못하여 잘못된 값을 다음 셀에게 전달하게 되면 그 뒤의 셀들이 모두 잘못된 값을 예측할 수 있다.

이러한 문제점을 해결하는 것이 Teacher Forcing.


입력으로 앞의 셀의 출력을 넣는 것이 아니라

ground truth 값을 차례로 입력한다.

이렇게 되면 어떤 셀이 잘못된 예측을 하더라도 다음 셀로 그 값이 넘어가지 않는다.

___

지금 트랜스포머에서 이러한 방식을 사용하고 있기 때문에 

결국 디코더 첫번째 레이어에 정답을 어떻게 제공하고 있는지를 보면 될 것이라고 생각함

## deepsaber-master/models/transformer/Layers.py

~~~
class DecoderLayer(nn.Module):

    def __init__(self, d_model, d_inner, n_head, d_k, d_v, dropout=0.1):
        super(DecoderLayer, self).__init__()
        self.slf_attn = MultiHeadAttention(n_head, d_model, d_k, d_v, dropout=dropout)
        self.enc_attn = MultiHeadAttention(n_head, d_model, d_k, d_v, dropout=dropout)
        self.pos_ffn = PositionwiseFeedForward(d_model, d_inner, dropout=dropout)

    def forward(self, dec_input, enc_output, non_pad_mask=None, slf_attn_mask=None, dec_enc_attn_mask=None):
        dec_output, dec_slf_attn = self.slf_attn(
            dec_input, dec_input, dec_input, mask=slf_attn_mask)
...
~~~

dec_input

___

## deepsaber-master/models/transformer/Models.py

~~~
class Decoder(nn.Module):
    ''' A decoder model with self attention mechanism. '''

    ...
    def forward(self, tgt_seq, tgt_input_seq, tgt_pos, src_mask, tgt_mask, enc_output, return_attns=False):

        dec_slf_attn_list, dec_enc_attn_list = [], []

        # -- Prepare masks
        non_pad_mask = get_non_pad_mask(tgt_seq)

        slf_attn_mask_subseq = get_subsequent_mask(tgt_seq)
        slf_attn_mask_keypad = get_attn_key_pad_mask(seq_k=tgt_mask, seq_q=tgt_mask)
        slf_attn_mask = (slf_attn_mask_keypad.byte() + slf_attn_mask_subseq.byte()).gt(0)

        dec_enc_attn_mask = get_attn_key_pad_mask(seq_k=src_mask, seq_q=tgt_seq)

        # -- Forward
        dec_output = self.tgt_word_emb(tgt_input_seq) + self.position_enc(tgt_pos)

        for dec_layer in self.layer_stack:
            dec_output, dec_slf_attn, dec_enc_attn = dec_layer(
                dec_output, enc_output,
                non_pad_mask=non_pad_mask,
                slf_attn_mask=slf_attn_mask,
                dec_enc_attn_mask=dec_enc_attn_mask)
    
    ...

~~~

dec_output이 tgt_input_seq로 임베딩 하고 거기에 포지셔널 인코딩 한거

결국 tgt_input_seq이 raw_ground_truth

~~~
class Transformer(nn.Module):
    ''' A sequence to sequence model with attention mechanism. '''

    ...

    def forward(self, src_seq, src_mask, src_pos, tgt_input_seq, tgt_seq, tgt_mask, tgt_pos):

        # print(tgt_seq, tgt_input_seq, tgt_mask, tgt_pos)

        tgt_seq, tgt_input_seq, tgt_mask, tgt_pos = tgt_seq[:, :-1], tgt_input_seq[:, :-1], tgt_mask[:, :-1], tgt_pos[:, :-1]

        enc_output, *_ = self.encoder(src_seq, src_mask, src_pos)
        if self.tgt_vector_input:
            dec_output, *_ = self.decoder(tgt_seq, tgt_input_seq, tgt_pos, src_mask, tgt_mask, enc_output)
        else:
            dec_output, *_ = self.decoder(tgt_seq, tgt_seq, tgt_pos, src_mask, tgt_mask, enc_output)
        seq_logit = self.tgt_word_prj(dec_output) * self.x_logit_scale
        # print(seq_logit.shape)
        # print(seq_logit[0,-1,50:61])

        return seq_logit.view(-1, seq_logit.size(2))
~~~

tgt_vector_input이 true이면 따로 정답 값을 알려주고, false이면 그냥 tgt_seq를 같이 넣음

## deepsaber-master/models/transformer_model.py

~~~
...
class TransformerModel(BaseModel):

    def __init__(self, opt):
        super().__init__(opt)
        self.opt = opt
        self.loss_names = ['ce']
        self.metric_names = ['accuracy']
        self.module_names = ['']  # changed from 'model_names'
        self.schedulers = []
        self.net = Transformer(
                d_tgt=opt.d_tgt,
                d_src=opt.d_src,
                n_tgt_vocab=opt.tgt_vocab_size,
                n_src_vocab=0,
                len_max_seq=opt.max_token_seq_len,
                src_vector_input=opt.src_vector_input,
                tgt_vector_input=opt.tgt_vector_input,
                tgt_emb_prj_weight_sharing=opt.proj_share_weight,
                emb_src_tgt_weight_sharing=opt.embs_share_weight,
                d_k=opt.d_k,
                d_v=opt.d_v,
                d_model=opt.d_model,
                d_word_vec=opt.d_word_vec,
                d_inner=opt.d_inner_hid,
                n_layers=opt.n_layers,
                n_head=opt.n_head,
                dropout=opt.dropout)
...
~~~

opt에 tgt_vector_input 저장되어 있음

확인 결과 false

결국 정답값으로 같은 값이 들어가게 된다.

tgt_seq 파악해야함

# deepsaber-master/models/transformer_model.py

target_block_sequence == src_mask == src_pos == tgt_seq

target_block_sequence_

target_

data['target']