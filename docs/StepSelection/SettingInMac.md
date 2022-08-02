# First Setting in Mac

## 패키지 설치 

가상환경 안에서 아래 명령 차례로 입력

~~~
  cd deepsaber-master/
  brew install megatools
  megadl 'https://mega.nz/#!tJBxTC5C!nXspSCKfJ6PYJjdKkFVzIviYEhr0BSg8zXINBqC5rpA'
  unzip pretrained_weights_latest.zip
  rsync -a pretrained_weights_latest/* scripts/training
  rm -r pretrained_weights_latest pretrained_weights_latest.zip
  mkdir songs
  brew install sox ffmpeg  
~~~

참고 : 기존 코드는 mv를 써서 training으로 옮기는데, 이미 그안에 내용물이 있는 경우에는 동작하지 않음, 그래서 rsync로 변경함

## 디버깅 실행 경로 변경

디버깅 전에 launch.json 설정

~~~
{
    // IntelliSense를 사용하여 가능한 특성에 대해 알아보세요.
    // 기존 특성에 대한 설명을 보려면 가리킵니다.
    // 자세한 내용을 보려면 https://go.microsoft.com/fwlink/?linkid=830387을(를) 방문하세요.
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "cwd" : "${fileDirname}"
        }
    ],
}
~~~

설정이 적용이 안되면 창 다시 로드 진행

## generated

generation 안에 generated 폴더 만들기