# soprize season11 doyouknowclub

## 소개
 소프라이즈 시즌 11 [한국에 '리액션' 하고 있는 이들은 누구인가요?](https://alook.so/posts/NG1t8M)에 대한</br>
 답변을 작성하기 위한 데이터 수집/가공/분석 과정을 공개하는 리포지토리입니다.
 
 </br>

## 따라해보기

### 1. 실행에 필요한 패키지 설치
 ```
 pip install -r requirements.txt
 ```
 </br>

 저의 경우에는 dlib도 설치했는데, 윈도에서 pip install로 dlib을 설치하기는 상당히 귀찮기 때문에</br>
 dlib을 설치하시려는 분들께서는 [Anaconda](https://www.anaconda.com/)를 설치하신 후</br>
 
 ```
 conda install -c conda-forge dlib
 ```
 
 을 살포시 입력해주시기 바랍니다.
 
 </br>

### 2. Youtube Data API 키 생성 및 secret 파일 만들기
 [Youtube Data API 안내 페이지](https://developers.google.com/youtube/v3/getting-started?hl=ko)의 설명을 따라 API 키를 발급받으세요.</br>
 API 키를 안전하게 입력하는 방법은 아주 많지만 저의 경우에는</br>
 무지성으로 secret.py 파일을 만들어 입력하는 방법을 선택했습니다.</br>
 secret.py는 .gitignore에 포함되어 있으니 git push를 통해 업로드되는 불상사는 막을 수 있습니다.</br>
 secret.py를 README.md와 같은 경로에 새로 추가하고 아래의 형식으로 API 키를 입력해주세요.</br>
 ```
 API_KEY = "여러분의 API 키"
 ```

</br>

### 3. 실행하기
 **1단계**</br>
 ```
 python search_video.py
 ```
 </br>

 **2단계**</br>
 ```
 python download_video.py
 ```
 </br>

 **3단계**</br>
 ```
 python extract_frames.py
 ```
 </br>

 **4단계**</br>
 추출된 프레임에서 사람 얼굴을 crop해야 합니다. 저의 경우에는 [StyleGAN-Encoder](https://github.com/pbaylies/stylegan-encoder)를 활용했습니다.</br>
 **stylegan-encoder**를 활용하실 경우에는 **dlib 설치가 필요**합니다.</br>
 stylegan-encoder를 새로운 경로에서 clone하신 뒤 해당 폴더에서</br>
 
 ```
 python align_image.py [extracted_frames까지의 경로] [result폴더까지의 경로 + face_crop]
 ```
 </br>
 경로를 입력하실때 []은 제외하시면 됩니다.</br>
 stylegan-encoder와 이 리포지토리가 같은 경로에 설치돼있을 시의 예시</br>
 
 
 *windows:*</br>
 
 ```
 python align_image.py ..\soprize-season11-doyouknowclub\result\extracted_frames ..\soprize-season11-doyouknowclub\result\face_crop
 ```
 </br>

 *mac/linux:*</br>
 
 ```
 python align_image.py ../soprize-season11-doyouknowclub/result/extracted_frames ../soprize-season11-doyouknowclub/result/face_crop
 ```
 
 </br>

 **5단계**</br>
 크롭된 얼굴 사진을 같은 인물별로 군집화해야합니다. 이를 위해 각 얼굴 이미지의 Representational Vector를 Spherical K-means로 군집화해보려</br>
 시도했으나 실패했고, 결국 Adobe Lightroom의 인물별 정렬 기능을 활용해 분류했습니다. 군집화된 결과는 리포지토리에 포함했습니다.</br>
 
 </br>
 
 **6단계**</br>
 ```
 python preprocess_images.py
 ```
 
 </br>
 
 **7단계**</br>
 jupyter notebook을 실행하고 indivisual_analysis.ipynb를 따라 데이터 분석/시각화를 하시면 됩니다.
