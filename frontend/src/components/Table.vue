<script>
  import userService from '@/services/service';
  import UserFormModal from '@/components/Modal.vue';

  export default {
    components: {
      UserFormModal,
    },

    data() {
      return {
        users: [],
        showModal: false,
        selectedUser: null,
        isEdit: false,
      };
    },

    created() {
      this.fetchUsers();
    },

      methods: {
        async fetchUsers() {
          try {
            const users = await userService.getUsers();
            this.users = users;
          } catch (error) {
              console.error('Error while trying to get the users:', error);
              alert('Error fetching users.');
          }
        },

      openCreateModal() {
        this.isEdit = false;
        this.selectedUser = null;
        this.showModal = true;
      },

      openEditModal(user) {
        this.isEdit = true;
        this.selectedUser = user;
        this.showModal = true;
      },

      closeModal() {
        this.showModal = false;
        this.selectedUser = null;
      },

      async handleSubmit(userData) {
        try {
          if (this.isEdit) {
            await userService.updateUser(userData.username, userData);
            alert('User updated.');
          } else {
              await userService.createUser(userData);
              alert('User created.');
          }

          this.closeModal();
          this.fetchUsers();

        } catch (error) {
            console.error('Error submitting data:', error);
            alert('Error submitting data.');
        }
      },

      async deleteUser(username) {
        if (confirm(`Are you sure you want to delete ${username}?`)) {
          try {
            await userService.deleteUser(username);
            this.fetchUsers();
          } catch (error) {
              console.error('Error while deleting:', error);
              alert('Error while deleting user');
          }
        }
      },
    },
  };
</script>

<template>
  <div>
    <h1>Users</h1>
    <button @click="openCreateModal">Create User</button>
      <!--
      A table listing all the users with the following columns:

      Username | Roles | Timezone | Is Active? | Last Updated At | Created At | Actions 
      
      -->
    <table v-if="users.length">
      <thead>
        <tr>
          <th>Username</th>
          <th>Roles</th>
          <th>Timezone</th>
          <th>Is Active?</th>
          <th>Last Updated At</th>
          <th>Created At</th>
          <th>Actions</th>
        </tr>
      </thead>

      <tbody>
        <tr v-for="user in users" :key="user.username">
          <td>
            <router-link :to="`/users/${user.username}`">{{ user.username }}</router-link>
          </td>
          <td>{{ user.roles.join(', ') }}</td>
          <td>{{ user.preferences.timezone }}</td>
          <td>{{ user.active ? 'Yes' : 'No' }}</td>
          <td>{{ new Date(user.updated_at * 1000).toLocaleString() }}</td>
          <td>{{ new Date(user.created_ts * 1000).toLocaleString() }}</td>
          <td>
            <button @click="openEditModal(user)">Edit</button>
            <button @click="deleteUser(user.username)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>

    <UserFormModal
      :show="showModal"
      :user="selectedUser"
      :isEdit="isEdit"
      @submit="handleSubmit"
      @close="closeModal"
    />
  </div>
</template>

