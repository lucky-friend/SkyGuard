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
    # ppyoloe-r
    run_cmd('CUDA_VISIBLE_DEVICES=0 python -u PaddleDetection/tools/train.py -c PaddleDetection/configs/rotate/ppyoloe_r/ppyoloe_r_crn_l_3x_dota.yml --use_vdl=true --vdl_log_dir=vdl_dir/scalar')
    
    
    # s2anet
    # run_cmd('CUDA_VISIBLE_DEVICES=0 python -u PaddleDetection/tools/train.py -c PaddleDetection/configs/rotate/s2anet/s2anet_1x_spine.yml --use_vdl=true --vdl_log_dir=vdl_dir/scalar')
    
    
    # fcosr
    # run_cmd('CUDA_VISIBLE_DEVICES=0 python -u PaddleDetection/tools/train.py -c PaddleDetection/configs/rotate/fcosr/fcosr_x50_3x_dota.yml --use_vdl=true --vdl_log_dir=vdl_dir/scalar')


