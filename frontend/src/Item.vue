<template>
  <div id="item">
    {{listId}}
    <blockquote>{{listName}}</blockquote>
    <ul>
      <li>
        <input placeholder="接下来做什么？" autofocus="true" @keyup.13="new_todo()" v-model="inputText" class="new">
      </li>

      <li v-for="item in todoList" :class="{finished: item.done}">
        <input type="checkbox" id="item.id" v-model="item.done" @change="updateTodo(item.id, item.done)">
        <label for="item.id"> {{item.text}}</label>
        <button class="deleteTodo" @click="deleteTodo(item.id)">X</button>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    data(){
      return {
        inputText: '',
      }
    },
  props:{
      listId: Number,
      todoList: Array,
      listName: String
  },
  methods: {
    new_todo(){
      axios
        .post('http://192.168.188.45:5000/new_todo',{
          todo_list_id: this.listId,
          text: this.inputText
        })
        .then(response => (console.log(response)))
        .catch(error => console.log(error));
      this.inputText = '';
    },
    deleteTodo(id){
      axios
        .delete('http://192.168.188.45:5000/delete_todo/' + id)
        .then(resp => (console.log(resp)))
        .catch(error => console.log(error))
    },
    updateTodo(id, done){
      axios.put('http://192.168.188.45:5000/update_todo/' + id, {
        done: done
        })
        .then(resp => console.log(resp))
        .catch(error => console.log(error))
    }
  }
}
</script>

<style scoped>
#item{
  float: right;
  width: 75%;
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
