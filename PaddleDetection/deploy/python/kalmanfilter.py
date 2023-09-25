import numpy as np
class KalmanFilter:
    def __init__(self):
        self.dt = 0.034  # 时间间隔

        # 状态转移矩阵
        self.A = np.array([
            [1, 0, self.dt, 0],
            [0, 1, 0, self.dt],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

        # 观测矩阵
        self.H = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0]
        ])

        # 系统噪声协方差矩阵
        self.Q = np.eye(4) * 0.001

        # 观测噪声协方差矩阵
        self.R = np.eye(2) * 10

        # 初始化状态向量和协方差矩阵
        self.x = np.zeros((4, 1))
        self.P = np.eye(4)

    def predict(self):
        self.x = np.dot(self.A, self.x)
        self.P = np.dot(np.dot(self.A, self.P), self.A.T) + self.Q
        return self.x

    def update(self, z):
        y = z - np.dot(self.H, self.x)
        S = np.dot(np.dot(self.H, self.P), self.H.T) + self.R
        K = np.dot(np.dot(self.P, self.H.T), np.linalg.inv(S))
        self.x = self.x + np.dot(K, y)
        self.P = self.P - np.dot(np.dot(K, self.H), self.P)