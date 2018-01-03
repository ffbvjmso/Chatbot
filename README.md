# TOC Project

A telegram bot based on a finite state machine

## Finite State Machine
![fsm](./img/show-fsm.png)

## Usage
The initial state is set to `user`.



* user
	* Input: "rabbit"
		* Reply: "You choose rabbit!" and go to `rabbit` state

	* Input: "cat"
		* Reply: "You choose cat" and go to `cat` state

	* Input: "dog"
		* Reply: "You choose dog" and go to `dog` state
* rabbit/cat/dog
	* Input: "A/B/C"
		* Show the link of the website and go to the corresponding state

	* Input: "E"
		* Return to the `user` state

* rabbit1/rabbit2/cat1/cat2/dog1/dog2
	* Input: "R"
		*Return to `rabbit/cat/dog`

	* Input: "M"
		*Go to `rabbit3/cat3/dog3`

	* Input: "E"
		*Go back to `user` state
* rabbit3/cat3/dog3
	* Input: "R"
		*Return to `rabbit/cat/dog`

	* Input: "E"
		*Return to `user` state
