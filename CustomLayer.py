import tensorflow as tf
from tensorflow.keras.layers import Input, Dense, MultiHeadAttention, GlobalAveragePooling1D, Embedding, LayerNormalization, Dropout
from tensorflow.keras.models import Model

class TransformerEncoderLayer(tf.keras.layers.Layer):
    def __init__(self, d_model, num_heads, ff_dim, rate=0.1):
        super(TransformerEncoderLayer, self).__init__()
        self.mha = MultiHeadAttention(num_heads=num_heads, key_dim=d_model)
        self.ffn = tf.keras.Sequential([
            Dense(ff_dim, activation='relu'),
            Dense(d_model)
        ])
        
        self.layernorm1 = LayerNormalization(epsilon=1e-6)
        self.layernorm2 = LayerNormalization(epsilon=1e-6)
        
        self.dropout1 = Dropout(rate)
        self.dropout2 = Dropout(rate)

    def call(self, x):
        attn_output = self.mha(x, x)  # Self-attention
        attn_output = self.dropout1(attn_output, training=True)
        out1 = self.layernorm1(x + attn_output)  # Add & Norm
        
        ffn_output = self.ffn(out1)
        ffn_output = self.dropout2(ffn_output, training=True)
        out2 = self.layernorm2(out1 + ffn_output)  # Add & Norm
        
        return out2