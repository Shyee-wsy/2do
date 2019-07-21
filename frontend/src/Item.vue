<template>
  <div id="item">
    <blockquote>Todo</blockquote>
    <ul>
      <li><input placeholder="接下来做什么？" autofocus="true"></li>
      <li v-for="item in todoList" :key="item.id" :class="{liFinished: finished}">
        <button :class="{finish: finished}" @click="toggleFinish"></button>
        {{item.content}}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
    data(){
      return {
        todoList:[
          {id: 0, content: '做饭'},
          {id: 1, content: '洗碗'},
          {id: 2, content: '浇花'}
        ],
        finished: false,
      }
    },
  props:{
  },
  methods: {
      toggleFinish: function () {
        this.finished = !this.finished;
      }
  }
}
</script>

<style scoped>
.finish{
  background-color: #228be8;
}
#item{
  float: right;
  width: 80%;
  height: 100%;
  border-right: 1px solid #7e7e81;
  background-color: #fff;
}
button{
  width: 20px;
  height: 20px;
  border-radius:20px;
  border: 1px solid #228be8;
  margin-right: 10px;
  outline: none;
  background-color: white;
}
blockquote{
  margin-top: 50px;
}
.liFinished{
  text-decoration: line-through;
}
</style>
