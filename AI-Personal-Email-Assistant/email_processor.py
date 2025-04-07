from transformers import GPT2LMHeadModel, GPT2Tokenizer

def generate_reply(email_content):
    try:
        model_name = 'gpt2'  # model to use
        model = GPT2LMHeadModel.from_pretrained(model_name)  # load model
        tokenizer = GPT2Tokenizer.from_pretrained(model_name)  # load tokenizer

        # encode email content to model input format
        inputs = tokenizer.encode(email_content, return_tensors='pt')

        # generate response from model
        outputs = model.generate(inputs, max_length=200, num_return_sequences=1)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)

        return response

    except Exception as e:
        print(f"Error loading model or tokenizer: {e}")  # error handling
        return None
