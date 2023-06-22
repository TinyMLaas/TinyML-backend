import docker
import json
import os
import tarfile

client = docker.from_env()

def build_image(dataset_path, model_path):
    try:
        image = client.images.get("tensorflow_tinymlaas")
        print("Using current image.")
    except Exception:
        try:
            res = client.images.build(
                path=".",
                dockerfile="compiling.Dockerfile",
                tag="tensorflow_tinymlaas",
                rm=True
                )
            print(res)

        except Exception as exc:
            print("Building failed:", exc)


def run_container():
    try:
        # check if there is already a tensorflow_tinymlaas and remove if exists
        try:
            container = client.containers.get("tensorflow_tinymlaas")
            container.remove(force=True)
        except Exception as exc:
            print("Because", exc , "we create a new container")

        # volumes can't mount subfolders, so we need to mount the relevant subfolders one by one
        res = client.containers.run(
            image="tensorflow_tinymlaas",
            name="tensorflow_tinymlaas",
            volumes=[
                #"TinyMLaaS_main:/TinyMLaaS_main",
                "/compiled_models:/compiled_models"
            ],
            tty=True,
            detach=True
        )

        print(res)

    except Exception as exc:
        print("Running failed:", exc)


def execute_command(dataset_path, output_path, model_path, model_params, model_name):
    try:
        container = client.containers.get("tensorflow_tinymlaas")

        # put needed files into running container
        with tarfile.open("/dataset_and_model.tar", "w") as f:
             f.add(dataset_path)
             f.add(model_path)
        
        with open("/dataset_and_model.tar", "rb") as f:
             container.put_archive(path=".", data=f) 

        params = json.dumps(model_params)
        command = f"""
            python TinyMLaaS_main/compiling.py 
            {model_path} {output_path} {dataset_path} \' {params} \' {model_name}
            """

        res = container.exec_run(
            cmd = command,

        )

        print(res)

        # the easiest way of getting the output to local
        # filesystem is to export it as a tar

        path = f"./{output_path}/{model_name}"

        if not os.path.exists(path):
            os.mkdir(path)

        bits, stat = container.get_archive(
            path=path
        )

        with open(f"{path}/compiled_model.tar", "wb") as f:
            for chunk in bits:
                f.write(chunk)

        with tarfile.open(f"{path}/compiled_model.tar", "r") as tar_f:
            tar_f.extractall(path=output_path)

        container.remove(force=True)
        
    except Exception as e:
        print("Execution failed:", e)
