import base64

import tensorflow as tf
from flask import Flask
from flask import jsonify
from flask import request


def load_labels(filename):
    #Read in labels, one label per line."""
    return [line.rstrip() for line in tf.gfile.GFile(filename)]

def load_graph(filename):
    #Unpersists graph from file as default graph."""
    with tf.gfile.FastGFile(filename, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        tf.import_graph_def(graph_def, name='')

label='C:/tmp/output_labels.txt'
graph='C:/tmp/output_graph.pb'
input_layer='DecodeJpeg/contents:0'
output_layer='final_result:0'
num_top_predictions=1


app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
    labels = load_labels(label)
    load_graph(graph)

    message = request.get_json(force=True)
    encoded = message['image']
    decoded = base64.b64decode(encoded)

    sess = tf.Session()
    softmax_tensor = sess.graph.get_tensor_by_name(output_layer)
    predictions, = sess.run(softmax_tensor, {input_layer: decoded})

    # Sort to show labels in order of confidence
    top_k = predictions.argsort()[-num_top_predictions:][::-1]
    max_confident_id = max(top_k)
    predicted_label = labels[max_confident_id]
    confidence_score = predictions[max_confident_id]
    print(predicted_label,confidence_score)
    response = {
        'prediction': {
            'prediction': predicted_label,
            'value': str(confidence_score)
        }
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run()
