import paddle
from subprocess import run

def run_cmd( cmd_str='', echo_print=1):
    """
    执行cmd命令，不显示执行过程中弹出的黑框
    备注：subprocess.run()函数会将本来打印到cmd上的内容打印到python执行界面上，所以避免了出现cmd弹出框的问题
    :param cmd_str: 执行的cmd命令
    :return: 
    """

    if echo_print == 1:
        print('\n执行cmd指令="{}"'.format(cmd_str))
    run(cmd_str, shell=True)

if __name__ == '__main__':
    # run_cmd('python PaddleDetection/deploy/python/infer.py --model_dir=output_inference/infer1 --image_file=test7.jpg --threshold=0.2')
    run_cmd('python PaddleDetection/deploy/python/infer.py --model_dir=output_inference/infer1/ --video_file=test5.mp4 --thresh=0.35 --output_dir=detection_result/ --device=GPU')


