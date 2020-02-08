### 依赖

```markdown
virtualenv --no-site-packages env
```

### 开发环境
```markdown
pip install -r requirements/requirements.txt
```

### 生产环境
```markdown
pip install -r requirements/prod.txt
```


### 创建数据表
```markdown
python manage.py db upgrade
```
### 数据模型修改后执行
```markdown
python manage.py db migrate 

python manage.py db upgrade

```

### 启动
```markdown
python manage.py runserver
```


