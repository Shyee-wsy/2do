<template>
  <div id="item">
    <blockquote>Todo</blockquote>
    <ul>
      <li><input placeholder="接下来做什么？" autofocus="true" @keyup.13="new_todo()" v-model="text" class="new"></li>
      <li v-for="(item,index) in todoList" :class="{finished: item.done}">
        <input type="checkbox" id="item.id" v-model="item.done">
        <label for="item.id"> {{item.text}}</label>
        <button class="deleteTodo" @click="deleteTodo(item.index)">X</button>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
    data(){
      return {
        todoList:[
          {id: 0, text: '做饭', done: false },
          {id: 1, text: '吃饭', done: false },
          {id: 2, text: '洗碗', done: false }
        ],
        text: ''
      }
    },
  props:{
  },
  methods: {
    new_todo: function(){
      this.todoList.push({id: 3, text: this.text, done: false});
      this.text = '';
    },
    deleteTodo: function(index){
      this.todoList.splice(index, 1);
    }
  }
}
</script>

<style scoped>
/*.finish{*/
  /*background-color: #228be8;*/
/*}*/
#item{
  float: right;
  width: 80%;
  height: 100%;
  border-right: 1px solid #7e7e81;
  background-color: #fff;
}
blockquote{
  margin-top: 50px;
}
.finished{
  text-decoration: line-through;
}
.deleteTodo{
  width: 20px;
  height: 20px;
  border: none;
  outline: none;
  background-color: inherit;
  color: rgba(205, 30, 20, 0.99);
  font-weight: bold;
  position: absolute;
  right: 5%;
  font-size: 16px;
}
.new{
  width: 90%;
}
</style>
