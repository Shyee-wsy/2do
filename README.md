# frontend


**这个文件夹存放前端文件。**


* 创建前端项目的一些前置与命令：
    * 安装 [Node.js](https://nodejs.org/en/)
    * 安装 [yarn](https://yarnpkg.com/en/docs/install) or `npm install --global yarn`
    * 安装 @vue/cli: `yarn global add @vue/cli`
    * 安装 @vue/cli-init`yarn global add @vue/cli-init`
    * 生成一个项目: `vue init webpack-simple frontend`
    * 进入 frontend 文件夹后安装依赖: `yarn install`
    * 运行前端项目: `yarn run dev`
    * 修改静态资源目录与 fronted 同级: `path: path.resolve(__dirname, './dist'),` -> `path: path.resolve(__dirname, '../dist'),`
    * 打包静态资源: `yarn run build`
    * other: 
        * [yarn Docs](https://yarnpkg.com/en/docs)
        * [npm Docs](https://docs.npmjs.com/)


# backend


**这个文件夹存储后端文件**


* 创建后端项目需要的一些前置与命令: 
    * 安装 [Python](https://www.python.org/downloads/)
    * 安装 Pipenv: `pip install pipenv`
    * 创建项目环境: `pipenv install --python 3 flask`
    * 运行项目: `pipenv run python -m flask run`


# other

