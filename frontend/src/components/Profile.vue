<script>
    import userService from '@/services/service';
    import UserFormModal from '@/components/Modal.vue';

    export default {
        components: {
            UserFormModal,
        },

        data() {
            return {
                user: null,
                error: null,
                showModal: false,
            };
        },

        created() {
            this.fetchUser();
        },

        methods: {
            async fetchUser() {
                const username = this.$route.params.username;
                try {
                    const response = await userService.getUser(username);
                    this.user = response;
                } catch (error) {
                    console.error('Error while trying to get user:', error);
                    this.error = 'Error fetching the user.';
                }
            },

            openEditModal() {
                this.showModal = true;
            },

            closeModal() {
                this.showModal = false;
            },

            async handleSubmit(userData) {
                try {
                    await userService.updateUser(userData.username, userData);
                    alert('User updated');
                    this.closeModal();
                    this.fetchUser();
                } catch (error) {
                    console.error('Error while trying to update:', error);
                    alert('Error updating user.');
                }
            },

            async deleteUser() {
                if (confirm(`Are you sure you want to delete ${this.user.username}?`)) {
                    try {
                        await userService.deleteUser(this.user.username);
                        this.$router.push('/'); 
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
    <div v-if="user">
      <h1>{{ user.username }}</h1>
      <p><strong>Roles:</strong> {{ user.roles.join(', ') }}</p>
      <p><strong>Timezone:</strong> {{ user.preferences.timezone }}</p>
      <p><strong>Is Active:</strong> {{ user.active ? 'Yes' : 'No' }}</p>
      <p><strong>Created At:</strong> {{ new Date(user.created_ts * 1000).toLocaleString() }}</p>
      <p><strong>Last Updated At:</strong> {{ new Date(user.updated_at * 1000).toLocaleString() }}</p>
  
      <button @click="openEditModal">Edit</button>
      <button @click="deleteUser">Delete</button>
  
      <UserFormModal
        :show="showModal"
        :user="user"
        :isEdit="true"
        @submit="handleSubmit"
        @close="closeModal"
      />
    </div>

    <div v-else-if="error">
      <p>{{ error }}</p>
    </div>

    <div v-else>
      <p>Loading user data: </p>
    </div>
  </template>
  
