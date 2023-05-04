[Home](https://natnew.github.io/Awesome-Prompt-Engineering/)
## Intermediate Prompting
Intermediate prompting is an advanced technique in prompt engineering that enables AI models to generate more nuanced and complex outputs. 
There are several methods of intermediate prompting, including chain-of-thought, zero-shot, self-consistency, and least-to-most prompting. 
Chain-of-thought prompting involves breaking down a complex task into a sequence of smaller tasks and prompting the AI model with each task in succession. 
Zero-shot prompting, on the other hand, allows the model to generate outputs for tasks it has never seen before by training it on a diverse range of tasks. 
Self-consistency prompts ensure that the generated outputs are consistent with the input prompt. 
At the same time, least-to-most prompting helps avoid generating implausible outputs by prompting the model with a range of possible outputs and 
selecting the most likely correct. These methods can be combined to improve the accuracy and quality of AI-generated outputs, making intermediate 
prompting an essential technique for AI engineers looking to develop advanced AI models.

##### The ChatGPT Formula 
You are a ```{actor}```. You are performing ```{task}```. ```{system boundary}```

---
### Examples
#### Chain of Thought
> ```{child}```: Teach me about courage. <br>
> ```{parent}```: The brave man is not he who does not feel afraid, but he who conquers that fear. <br>
> ```{child}```: Teach me about kindness. <br>
> ```{parent}```: No act of kindness, no matter how small, is ever wasted. <br>
> ```{child}```: Teach me about adaptability. <br>
> ```{parent}```: The measure of intelligence is the ability to change. <br>
> ```{child}```: Teach me about strength. <br>

#### Zero Shot Chain of Thought
Re-write the instructions, delimited by triple backticks, in the following format: Step 1 — … Step 2 — … … Step N — …If the text does not contain a sequence of instructions, then simply write ”No steps mentioned.” <br>
```Preheat the oven to 180C/160C Fan/Gas 4. Grease and line two 20cm/8in sandwich tins. Break the eggs into a large mixing bowl, then add the sugar, flour, baking powder and butter. Mix together until well combined with an electric hand mixer (you can also use a wooden spoon), but be careful not to over mix. Put a damp cloth under your bowl when you’re mixing to stop it moving around. The finished mixture should fall off a spoon easily. Divide the mixture evenly between the tins: this doesn’t need to be exact, but you can weigh the filled tins if you want to check. Use a spatula to remove all of the mixture from the bowl and gently smooth the surface of the cakes. Bake the cakes on the middle shelf of the oven for 25 minutes. Check them after 20 minutes. The cakes are done when they’re golden-brown and coming away from the edge of the tins. Press them gently to check — they should be springy to the touch. Set aside to cool in their tins for 5 minutes. Run a palette or rounded butter knife around the inside edge of the tins and carefully turn the cakes out onto a cooling rack. To assemble the cake, place one cake upside down onto a plate and spread it with plenty of jam. If you want to, you can spread over whipped cream too. Top with the second cake, top-side up. Sprinkle over the caster sugar.```

---
### Notes
Feedback and suggestions are welcome! <br>
Create your prompts today.
Go to https://chat.openai.com and sign up/in <br
