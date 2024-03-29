'''
    1. 파이토치(PyTorch) 개요
        1) 파이썬의 넘파이(Numpy) 라이브러리처럼 과학 연산을 위한 라이브러리 공개 => 딥러닝 프레임워크로 발전
            - 넘파이를 대체하면서 GPU를 이용한 연산이 필요한 경우
            - 최대한 유연성, 속도를 제공하는 딥러닝 플랫폼이 필요한 경우
        2) GPU에서 텐서 조작및 동적 신경망 구축이 가능한 프레임워크
            - 딥러닝에서는 기울기 계산할 때 미분을 쓰는데, GPU를 사용하면 빠른 계산이 가능
            - 내부적으로 CUDA, cuDNN이라는 API를 통해 GPU를 연산에 사용할 수 있음
            - 병렬연산에서 GPU의 속도는 CPU의 속도보다 훨씬 빠르므로 딥러닝 학습에서 GPU사용은 필수임

    2. 텐서(Tensor)
        1) 파이토치의 데이터 형태
        2) 텐서는 단일 데이터 형식으로 된 자료들의 다차원 행렬

    3. 벡터
        - 인공지능(머신러닝/ 딥러닝 ) 에서 데이터는 벡터(vecto)로 표현
        - [1.0, 1.1, 1.2] 처럼 숫자들의 리스트, 1차원 배열 형태

       행렬(matrix)
        - 행과 열로 표현되는 2차원 배열 형태

       텐서
        - 3차원 이상의 배열 행태
            - 1차원의 축(행) : axis = 0 (벡터)
            - 2차원의 축(열) : axis = 1 (행렬)
            - 3차원의 축(채널) : axis = 2 (텐서)
        -torch.tensor()
        - 텐서간의 연산을 수행할 때, 기본적으로 두 텐서가 같은 장치에 있어야 함
        - 서로 다른 장치(device)에 있는 텐서끼리 연산을 수행하면 오류가 발생함

    4. 파이토치 특징
        1) 신경망은 연산 그래프를 이용하여 계산을 수행
        2) 네트워크가 학습될 때 손실함수의 기울기가 가중치와 바이어스(절편)를 기반으로 계산되며
           이후 경사 하강법을 사용하여 가중치가 업데이트됨
        3) 이 때 연산 그래프를 이용하여 이 과정이 효과적으로 수행
        4) 파이썬 환경과 쉽게 통합할 수 있음
        5) 모델 훈련을 위한 CPU사용률이 텐서플로와 비교하여 낮음
        6) 학습 및 추론 속도가 빠르고 다루기 쉬움

    5. 파이토치 아키텍처
        1) 파이토치 API 계층: 사용자의 편의성 여러 패키지들 제공
            - torch : GPU를 지원하는 텐서 패키지
                      CPU뿐만 아니라 GPU에서 연산이 가능 (빠른속도로 많은 양의 계싼이 가능)
                      파이토치에서는 텐서가 핵심
            - torch.autograd : 자동 미분 패키지
            - torch.nn : (neural network) 신경망 구축 및 훈련 패키지
            - troch.multiprocessing, torch.utils
        2) 파이토치 엔진(라이브러리)
            - C++로 감싼(래핑 wrapping) 다음 Python API 형태로 제공
    6. 텐서의 기본 속성
        1) 모양 (Shape)
        2) 자료형 (data type)
        3) 저장된 장치





'''
import torch

a= torch.tensor([1,2,3])
b= torch.tensor([4,5,6])
c= a+b
print(c)

print(torch.tensor([[1,2], [3,4]]))
# print(torch.tensor([[1,2], [3,4]], device="cuda:0")) : GPU가 없는데 GPU에 할당을 해주면 에러

print("------------------------------------")

data = [
    [1,2],
    [3,4]
]
x= torch.tensor(data)
