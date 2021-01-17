import tensorflow as tf

@tf.function
def macroSoftF1(y, y_hat):
    """Compute the macro soft F1-score as a cost (average 1 - soft-F1 across all labels).
    Use probability values instead of binary predictions.
    
    Args:
        y (int32 Tensor): targets array of shape (BATCH_SIZE, N_LABELS)
        y_hat (float32 Tensor): probability matrix from forward propagation of shape (BATCH_SIZE, N_LABELS)
        
    Returns:
        cost (scalar Tensor): value of the cost function for the batch
    """

    tf.print(y)
    tf.print(y_hat)
    
    y = tf.nn.softmax(tf.cast(y, tf.float32))
    y_hat = tf.nn.softmax(tf.cast(y_hat, tf.float32))

    tf.print(y)
    tf.print(y_hat)
    
    tp = tf.reduce_sum(y_hat * y, axis=0)
    fp = tf.reduce_sum(y_hat * (1 - y), axis=0)
    fn = tf.reduce_sum((1 - y_hat) * y, axis=0)
    soft_f1 = 2*tp / (2*tp + fn + fp + 1e-16)
    cost = 1 - soft_f1 # reduce 1 - soft-f1 in order to increase soft-f1
    macroCost = tf.reduce_mean(cost) # average on all labels
    return macroCost
