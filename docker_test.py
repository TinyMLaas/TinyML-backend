import docker

def do_a_tensorflow():

    client = docker.from_env()

    try:
        res = client.images.build(
            path=".",
            tag="tensorflow_tinymlaas",
            nocache=True
            )
        print(res)

    except Exception as e:
        print("Building failed:", e)

        
    try:
        # check if there is already a tensorflow_tinymlaas and remove if exists
        container = client.containers.get("tensorflow_tinymlaas")
        
        if container:
            container.remove(force=True)
        
        res = client.containers.run(
            image="tensorflow_tinymlaas",
            
            #volumes = {"/TinyMLaaS_main/": {"bind": "/TinyMLaaS_main"}, "mode": "rw"},
            volumes=[
                "TinyMLaaS_main:/TinyMLaaS_main",
                "data:/data",
                "tensorflow_models:/tensorflow_models",  
                "compiled_models:/compiled_models"
            ],
            name="tensorflow_tinymlaas",
            tty=True,
            detach=True,
            #remove=True
        )
        print(res)
        
    except Exception as e:
        print("Running failed:", e)

    try:
        container = client.containers.get("tensorflow_tinymlaas")
        
        params = str({"epochs": 1, "img_width": 96, "img_height": 96, "batch_size": 1})
        res = container.exec_run(
            cmd =f"""python TinyMLaaS_main/compiling.py tensorflow_models/1 compiled_models data/cars_dataset {params} /1""" 
            
            # f"""
            #     from TinyMLaaS_main import compiling.py; do_a_tensorflow(tensorflow_models/1, compiled_models, data/cars_dataset, {params}, /1)
            #     """
        )
        print(res)
        
    except Exception as e:
        print("Execution failed:", e)

    
do_a_tensorflow()