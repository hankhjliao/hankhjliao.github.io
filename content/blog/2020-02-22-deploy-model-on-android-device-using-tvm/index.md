---
Title: Deploy Model on Android Device using TVM
Date: 2020-02-22T21:00:00
Categories: Tutorial
Tags: tutorial
Slug: 2020-02-22-deploy-model-on-android-device-using-tvm
Summary: Build the TVM Docker container to ensure we has the same environment.
---

{{< figure src="deploy-model-on-android-device-using-tvm-result.png" caption="The schematic diagram of the result. The cat image is downloaded from [here](https://raw.githubusercontent.com/dmlc/mxnet.js/master/data/cat.png?raw=true)" >}}

## Build TVM Docker Container Environment

Build the TVM Docker container to ensure we has the same environment.

(You can skip this section if you know how to install the
[dependent package](https://github.com/apache/incubator-tvm/blob/master/docker/Dockerfile.demo_android)
and tvm4j. And you are familiar with the hierarchy of the folder of the tvm.)

1. Install Docker. https://docs.docker.com/install/

2. Clone the TVM repo.

   `$ git clone --depth 1 https://github.com/apache/incubator-tvm.git tvm`

3. Build the Docker image using the Dockerfile ``Dockerfile.demo_android`` in
   the folder ``tvm/docker``.

   `$ cd tvm/docker/`

   `$ bash ./build.sh demo_android -it bash`

4. Exit from the temp container using ``ctrl+D``.

5. Build the TVM Docker container and attach it.

   `$ docker run -it --name tvm tvm.demo_android`

   `$ docker start tvm && docker attach tvm`

6. Install tvm4j.

   `$ apt install maven`

   `$ cd /usr/tvm/`

   `$ make jvmdkg`

   `$ make jvminstall`

## Test the Model Running Well on TVM

1. Copy the onnx into the Docker container using
   [docker cp](https://docs.docker.com/engine/reference/commandline/cp/).

2. Install onnx.

   `$ pip3 install onnx`

3. Run the script below to test the model.

   ```python

   import onnx
   import numpy as np
   import tvm
   import tvm.relay as relay
   from tvm.contrib import graph_runtime

   # Change this to match the input of your model.
   input = np.ones([1,3,256,256])

   # Change this to match the filename of your model.
   onnx_model = onnx.load('model.onnx')

   # Change this to match the shape of input of your model.
   x = np.ones((1, 3, 256, 256))

   # Change this to match the input name of your model.
   input_name = 'input.1'

   target = 'llvm'
   shape_dict = {input_name: x.shape}
   sym, params = relay.frontend.from_onnx(onnx_model, shape_dict)
   ctx = tvm.context(target, 0)
   with relay.build_config(opt_level=0):
       intrp = relay.build_module.create_executor('graph', sym, ctx,  target)

   with relay.build_config(opt_level=2):
       graph, lib, params = relay.build_module.build(sym, target, params=params)

   dtype = np.float32
   module = graph_runtime.create(graph, lib, ctx)
   module.set_input(**params)

   module.set_input(input_name, tvm.nd.array(input.astype(dtype)))
   module.run()
   output = module.get_output(0).asnumpy()

   # May change this to match the output type of your model.
   print(output)
   ```

## Cross-compile the Model

Run the script below and you will get three files
(``model.so``, ``model.json``, ``model.params``).

   ```python

   import onnx
   import numpy as np
   import tvm
   import tvm.relay as relay

   # Change this to match the filename of your model.
   onnx_model = onnx.load('model.onnx')

   # Change this to match the shape of input of your model.
   x = np.ones((1, 3, 256, 256))

   # Change this to match the input name of your model.
   input_name = 'input.1'

   arch = 'arm64'
   target =  'llvm -target=%s-linux-android' % arch
   shape_dict = {input_name: x.shape}
   sym, params = relay.frontend.from_onnx(onnx_model, shape=shape_dict)

   with relay.build_config(opt_level=0):
      intrp = relay.build_module.create_executor('graph', sym, tvm.cpu(0), target)

   with relay.build_config(opt_level=2):
      graph, lib, params = relay.build_module.build(sym, target, params=params)

   libpath = 'model.so'

   # Change the parameter `cc` to match the architecture of your phone.
   # You can run `adb shell cat /proc/cpuinfo` to list the info of your CPU.
   # This is for Android SDK 28 (Pie) and CPU is aarch64.
   lib.export_library(libpath, cc='/opt/android-sdk-linux/ndk-bundle/toolchains/llvm/prebuilt/linux-x86_64/bin/aarch64-linux-android28-clang')

   graph_json_path = 'model.json'
   with open(graph_json_path, 'w') as fo:
      fo.write(graph)

   param_path = 'model.params'
   with open(param_path, 'wb') as fo:
      fo.write(relay.save_param_dict(params))
   ```


## Write the Android Program

In the folder ``tvm/apps/android_deploy``, you will see an example provided by
TVM. You can compile the Android program first to know what each functions
does, or you can modified the files according to
[README.md](https://github.com/apache/incubator-tvm/blob/master/apps/android_deploy/README.md)

Moreover, [here](https://github.com/hankhjliao/deploy-style-transfer-on-android)
is an Android program that I deployed the style transfer models which were
trained by [Tony Tseng](https://github.com/Tony-Tseng).

## Compile the Android Program

1. Change directory to the root of the android program.

   `$ cd /usr/tvm/apps/android_deploy`

2. Generate the apk file.

   `$ gradle clean build --no-daemon`

3. Create the key which is used to sign apk if you don't have.

   `$ bash ./dev_tools/gen_keystore.sh`

4. Sign the apk file.

   `$ bash ./dev_tools/sign_apk.sh`

5. The signed apk file will be
   ``./app/build/outputs/apk/release/tvmdemo-release.apk``

6. Copy the apk file from the Docker container.
