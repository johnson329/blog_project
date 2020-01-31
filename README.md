### 依赖

```markdown
virtualenv --no-site-packages env
pip install -r requirements.txt
```

### 启动
```markdown
python manage.py runserver
```
1.
解决flask循环引用问题的一种解决办法

http://www.pythondoc.com/flask-mega-tutorial/helloworld.html#id2

https://blog.csdn.net/u010900754/article/details/75089682

把import放到最后
2. 
gitignore有时候不起作用
git rm --cached 指定的文件
git rm -r --cached 指定的文件夹
https://blog.csdn.net/HXNLYW/article/details/98053888


