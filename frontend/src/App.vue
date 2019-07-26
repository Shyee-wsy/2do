<template>
  <div id="app">
    <div id="list">
      <ul>
        {{listId}}
        <li v-for="item in lists" :key="item.id" @click="getListId(item.id)">
          <button  v-if="item.id !== 1" class="deleteList" @click="deleteList(item.id)">X</button>
          {{ item.text }}
        </li>

        <li>
          <input placeholder="+ 新建清单" @keyup.13="newList(text)" v-model="text">
        </li>
      </ul>
    </div>
    <Item :listId="listId" :todoList="todoList" :listName="listName"></Item>
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
      listId: 3,
      text: '',
      todoList: [],
      listName: 'Todo'
    }
  },
  methods: {
    deleteList(id){
      axios
        .delete('http://192.168.188.45:5000/delete_list',{
          id: id
        })
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
      this.listId = id;
    }
  },
  mounted(){
    let data = [];
    axios
      .get('http://192.168.188.45:5000/get_todo')
      .then(response => {
        data = response.data;
        for(let i = 0; i < data.length; i++){
          this.lists.push({id: data[i].id, text: data[i].text} )
          if(data[i].id === this.listId){
            this.listName = data[i].text;
            let items = data[i].todo_items;
            for(let j = 0; j < items.length; j++){
              this.todoList.push({id: items[j].id, text: items[j].text, done: items[j].done})
            }
          }
        }
      })
      .catch(error => console.log(error));
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
