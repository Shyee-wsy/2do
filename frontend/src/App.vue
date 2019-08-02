<template>
  <div id="app">
    <div id="list">
      <ul>
        <li v-for="item in lists" :key="item.id" @click="getListId(item.id)">
          <button  v-if="item.id !== 1" class="deleteList" @click="deleteList(item.id)">X</button>
          {{ item.text }}
        </li>

        <li>
          <input placeholder="+ 新建清单" @keyup.13="newList(text)" v-model="text">
        </li>
      </ul>
    </div>
    <Item :listId="listId" :todoItems="todoItems" :listName="listName"></Item>
  </div>
</template>

<script>
import Item from './Item'
import axios from 'axios';

export default {
  name: 'app',
  components: {
    Item
  },
  data () {
    return {
      lists:[],
      listId: 1,
      text: '',
      todoItems: [],
      listName: 'Todo'
    }
  },
  methods: {
    deleteList(id){
      axios
        .delete('http://192.168.188.45:5000/delete_list/' + id)
        .then(response => console.log(response))
        .catch(error => console.log(error))
    },
    newList(text){
      axios
        .post('http://192.168.188.45:5000/new_list',{
          text: text
        })
        .then(response => (console.log(response)))
        .catch(error => console.log(error))
      this.text='';
    },
    getListId(id){
      this.listId = Number(id);
      this.listName = this.lists[id-1].text;
    },
    getData() {
      this.$server.getData().then(data =>{
              this.lists = data["todo_list"]
              this.todoItems = data[this.listId];
      })
      // let xhr = new XMLHttpRequest();
      // xhr.open('get', 'http://192.168.188.45:5000/get_todo', false)
      // xhr.send(null)
      // if((xhr.status >= 200 && xhr.status < 300) || xhr.status == 304){
      //   let data = JSON.parse(xhr.responseText);
      //   console.log(data);
      //   this.lists = data['todo_list'];
      //   this.todoItems = data[this.listId];
      // }
      // else{
      //   console.log("request was unsuccessful: " + xhr.status);
      // }

    }
  },
  mounted(){
    this.getData();
  },
  watch: {
    listId(){
      this.getData()
    }
  }
}
</script>

<style>
#app{
  width: 100vw;
  height: 100vh;
  margin: 0 auto;
}
#list{
  float: left;
  width: 25%;
  height: 100%;
  border-left: 1px solid #7e7e81;
  border-right: 1px solid #7e7e81;
  background-color: #f4f4f4;
}
*{
  box-sizing: border-box;
}
body{
  margin: 0;
}
ul li{
  border-bottom: 1px solid #7e7e81;
  list-style-type: none;
  height: 50px;
  padding: 20px;
  font-size: 20px;
}
input{
  border: none;
  padding: 5px;
  background-color: inherit;
  outline: none;
}
#list li:hover{
  font-weight: bold;
}
#list li:nth-child(1){
  margin-left: 20px;
}
#item ul li{
  margin-right: 30px;
  font-size: 16px;
  /*text-decoration: line-through;*/
}
li input {
  font-size: 16px;
}
.deleteList{
  background-color: inherit;
  border: none;
  color: rgba(205, 30, 20, 0.99);
  outline: none;
  margin-right: 2%;
}
</style>
