from flask import Flask,render_template,request,redirect,send_from_directory
import os

UPLOAD_DIR = os.path.dirname(__file__)+'/static/files' ##dir 디렉토리이름  __file__ 현재 파일의 경로를 말한다.
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR) ##해당 경로에 있는지 확인하고 없으면 만들어라.

app = Flask(__name__)

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/fileUpload',methods=['POST'])
def fileUpload():
    f = request.files['file']
    dirname = os.path.dirname(__file__) + '/static/files/' + f.filename
    print(dirname)
    f.save(dirname)
    return redirect('/filelist')

@app.route('/filelist')
def filelist():
    files=[]
    for filename in os.listdir(UPLOAD_DIR):
        path = os.path.join(UPLOAD_DIR,filename)
        if os.path.isfile(path):
            files.append(filename)

    return render_template('filelist.html',files=files)

@app.route('/static/files/<path:path>') ##이렇게 꺽새로 만들어두면 밑에 def함수에서 파라미터로 받아야한다.
def get_file(path):
    
    return send_from_directory(UPLOAD_DIR,path,as_attachment=True) ##파일명, 경로명, 세번쨰는 뭐지?

if __name__ == '__main__':
    app.run(debug=True,port=80)