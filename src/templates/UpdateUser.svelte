<script>
  import API from "../API";

  let searchString = "";
  let users = [];
  let selectedUser = null;

  async function onSearchClick() {
    users = await API.user.search(searchString);
  }

  let email = "";
  let firstName = "";
  let lastName = "";
  let payRate = null;
  let noShowDays = null;
  let callOutDays = null;
  let position = null;
  let forcePasswordChange = null;

  function onFirstNameInput(event) {
    firstName = event.target.value;
  }

  function onLastNameInput(event) {
    lastName = event.target.value;
  }

  function onPayRateInput(event) {
    payRate = event.target.value;
  }

  function onNoShowDayInput(event) {
    noShowDays = event.target.value;
  }

  function onCallOutDayInput(event) {
    callOutDays = event.target.value;
  }

  async function onSaveClick() {
    await API.user.update(
      selectedUser.id,
      firstName,
      lastName,
      payRate,
      noShowDays,
      callOutDays,
      position,
      forcePasswordChange
    );
  }

  function onUserSelect(user) {
    console.log(user);
    selectedUser = user;
    email = user.email;
    firstName = user.firstName;
    lastName = user.lastName;
    payRate = user.payRate;
    noShowDays = user.noShowDays;
    callOutDays = user.callOutDays;
    position = user.position.toLowerCase();
    forcePasswordChange = user.forcePasswordChange;
  }
</script>

<main>
  Edit User
  <hr />
  <div style="display: flex; flex-direction: row">
    <div style="width: 50%; padding: 8px">
      <input placeholder="Search by last name..." bind:value={searchString} />
      <button on:click={onSearchClick}> Search </button>
      <hr />
      {#each users as user}
        <button
          style={user == selectedUser ? "background-color:mediumseagreen;" : ""}
          on:click={() => {
            onUserSelect(user);
          }}
        >
          {user.lastName}, {user.firstName}
        </button>
        <br />
      {/each}
    </div>
    {#if selectedUser !== null}
      <div style="width: 50%; padding: 8px">
        <input
          type="text"
          placeholder="E-mail Address"
          value={email}
          disabled
        />
        <br />
        <input
          type="text"
          placeholder="First Name"
          value={firstName}
          on:input={onFirstNameInput}
        />
        <br />
        <input
          type="text"
          placeholder="Last Name"
          value={lastName}
          on:input={onLastNameInput}
        />
        <br />
        Pay Rate
        <input
          type="number"
          placeholder="Pay Rate"
          value={payRate}
          on:input={onPayRateInput}
        />
        <br />
        No Show Days
        <input
          type="number"
          placeholder="No Show Days"
          value={noShowDays}
          on:input={onNoShowDayInput}
        />
        <br />
        Call Out Days
        <input
          type="number"
          placeholder="Call Out Days"
          value={callOutDays}
          on:input={onCallOutDayInput}
        />
        <br />
        Position
        <select bind:value={position} disabled={selectedUser.id === 1}>
          <option value="associate">Associate</option>
          <option value="manager">Manager</option>
          <option value="administrator">Administrator</option>
        </select>
        <br />
        Force user to change password upon next log in
        <input type="checkbox" bind:checked={forcePasswordChange} />
        <br />
        <button on:click={onSaveClick}>
            Save
        </button>
      </div>
    {/if}
  </div>
</main>
