# 🦜 <만들면서 배우는 생성 AI 2판>의 코드 저장소

이 저장소는 한빛미디어에서 출간한 "만들면서 배우는 생성 AI 2판"의 코드를 담고 있습니다. ([교보문고](https://product.kyobobook.co.kr/detail/S000208953342), [Yes24](https://www.yes24.com/Product/Goods/122338458), [알라딘](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=324278784), [한빛미디어](https://www.hanbit.co.kr/media/books/book_view.html?p_code=B6550508630))

책을 구매하시면 꼭 [에러타 페이지](https://tensorflow.blog/gen-dl-2/)를 확인해 주세요.

1판의 깃허브는 [여기](https://github.com/rickiepark/GDL_code/)입니다.

<img src="cover.jpeg" width=600>

## 목차
PART 1: 생성 딥러닝 소개
* 1장: 셍성 모델링
* 2장: 딥러닝
  * [다층 퍼셉트론](notebooks/02_deeplearning/01_mlp/mlp.ipynb)
  * [합성곱](notebooks/02_deeplearning/02_cnn/convolutions.ipynb)
  * [합성곱 신경망](notebooks/02_deeplearning/02_cnn/cnn.ipynb)

PART 2: 6가지 생성 모델링 방식
* 3장: 변이형 오토인코더
  * [오토인코더](notebooks/03_vae/01_autoencoder/autoencoder.ipynb)
  * [변이형 오토인코더 - 패션 MNIST](notebooks/03_vae/02_vae_fashion/vae_fashion.ipynb)
  * [변이형 오토인코더 - CelebA](notebooks/03_vae/03_vae_faces/vae_faces.ipynb)
* 4장: 생성적 적대 신경망
  * [DCGAN](notebooks/04_gan/01_dcgan/dcgan.ipynb)
  * [WGAN-GP](notebooks/04_gan/02_wgan_gp/wgan_gp.ipynb)
  * [CGAN](notebooks/04_gan/03_cgan/cgan.ipynb)
* 5장: 자기 회귀 모델
  * [LSTM](notebooks/05_autoregressive/01_lstm/lstm.ipynb)
  * [PixelCNN](notebooks/05_autoregressive/02_pixelcnn/pixelcnn.ipynb)
  * [PixelCNN - 혼합 분포](notebooks/05_autoregressive/03_pixelcnn_md/pixelcnn_md.ipynb)
* 6장: 노멀라이징 플로 모델
  * [RealNVP](notebooks/06_normflow/01_realnvp/realnvp.ipynb)
* 7장: 에너지 기반 모델
* 8장: 확산 모델

PART 3: 생성 모델링의 응용 분야
* 9장: 트랜스포머
* 10장: 고급 GAN
* 11장: 음악 생성
* 12장: 월드 모델
* 13장: 멀티모달 모델
* 14장: 결론

각 장의 노트북에는 구글 코랩에서 실행할 수 있는 링크가 포함되어 있습니다.
