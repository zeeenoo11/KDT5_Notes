
## OpenCV 다루기

1. 그림 파일 출력

2. 그림 그리기
    1) 직선 그리기
        ```python
        cv2.line(img, start, end, color, thickness)
        ```
    2) 사각형 그리기
        ```python
        cv2.rectangle(img, start, end, color, thickness)
        ```
    3) 원 그리기
        ```python
        cv2.circle(img, center, radius, color, thickness)
        ```
    4) 타원 그리기
        ```python
        cv2.ellipse(img, center, axes, angle, startAngle, endAngle, color, thickness)
        ```
    5) 다각형 그리기
        ```python
        cv2.polylines(img, points, isClosed, color, thickness)
        ```
    6) 단어 입력
        ```python
        cv2.putText(img, text, org, font, fontScale, color)
        ```

4. 그림 파일 저장하기

## 얼굴 인식

1. 얼굴 인식 클래스 : cv2.CascadeClassifier
    - 모델 파일 : haarcascade_frontalface_default.xml
    - 얼굴 검출 : detectMultiScale(image, scaleFactor, minNeighbors, flags, minSize, maxSize)

2. 눈 인식 클래스도 있음 : haarcascade_eye.xml

## CNN 이미지 인식

1. DNN의 한계 : 실제 이미지보다 배경 데이터가 더 많다

2. CNN의 개념
    - Convolutional Neural Network : 이미지 인식에 특화된 신경망
    - Convolution : 이미지의 특징을 추출; 얼굴 인식처럼 ROI를 추출

3. Convolution Layer
    - 이미지의 특징을 추출하는 계층
    - (0,0)부터 시작하여 필터를 이동시키면서 특징을 추출
    - 주요 특징만 추출 -> 1차원으로 Linear에 전달
    - 구성
      1) 커널/필터/마스크 : 3x3, 5x5의 이미지 위를 이동하는 행렬
      2) 스트라이드 : 필터 이동 방향 및 크기; 왼쪽에서 오른쪽으로 1 픽셀 씩 이동 (3x3 or 5x5 기준 1)
    - grayscale 이미지 : 1채널
      - 가중합을 한 픽셀로 출력
    - RGB 이미지 : 3채널
      - 3개의 필터로 각 채널을 합산하여 출력
    - Padding : 이미지의 테두리를 0으로 채워서 이미지 크기를 유지
      - 모서리의 이미지의 특징을 유지하기 위해 사용
      - valid : 입력과 출력 이미지의 크기가 다르게 패딩
      - same : 출력 이미지와 입력 이미지의 크기가 같도록 패딩 (0)

4. 차원
    1) Conv1D : 1차원 데이터의 특징 추출
        - 시간을 축으로 좌우로만 이동
    2) Conv2D : 2차원 데이터의 특징 추출
        - 똑같이 좌우로 이동, 합성곱
    3) Conv3D : 3차원 데이터의 특징 추출
        - 동영상 데이터의 특징 추출

5. Pooling Layer : resize 역할
    - Convolution Layer의 출력 이미지를 입력으로 받아 크기를 줄이는 역할
    - Max Pooling : 최대값을 추출
    - Average Pooling : 평균값을 추출
    - 보통 2x2로 설정

6. Flatten Layer : 1차원으로 변환
    - Convolution Layer의 출력 이미지를 1차원으로 변환

=> input -> Convolution -> Pooling -> Flatten -> Dense(얘는 뭐지) -> output





 
