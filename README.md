# Highlight_finder
opencv 기반 하이라이트 영상 레이블링 자동화 도구

## Requirements
```
$ pip install opencv-python
```
## Usage
```
$ python Highlight_finder.py file_name.txt
```
- file_name.txt : url, 저장할 이름이 저장된 txt파일. 
이전 다운로드에서 사용한 파일에서 하이라이트 부분만 지우시면 됩니다.

## txt file format
url1,save_file_name1
url2,save_file_name2
...

예시
```
https://tv.naver.com/v/12204239,T1 vs DWG 1세트
https://tv.naver.com/v/12204239,T1 vs DWG 2세트
```

## Output
Output File: ./data/GameVideoName.txt
```
시작 프레임,끝 프레임, 시작 시간, 끝 시간
```
## Cautions
 - 위의 기준은 풀 영상입니다.
 - csv파일 연동 및 텍스트파일 형식 바꾸고 싶으신 분들은 요청해주세요.

## For Jupyter Notebook
- 실행 후 '텍스트 파일 이름'을 입력하면 다운로드가 시작됩니다.

