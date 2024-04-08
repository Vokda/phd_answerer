This is a llama2 model parameterized to answer questions for my cousin's PhD thesis in theoretical physics.
You can find the thesis [here](https://portal.research.lu.se/en/publications/multi-meson-dynamics-in-chiral-perturbation-theory).

Run `create_model.sh` to generate a model that can be run with ollama.

Run `import_and_run.py` to boot up the AI. It will import the thesis, vectorize it and they prompt the user for a question. Kill the program to exit it. 
There is of course nothing stopping you from using another thesis
