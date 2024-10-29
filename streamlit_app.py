import streamlit as st
import boto3

st.title("Amazon Bedrock Integration with Streamlit")

bedrock = boto3.client(
    service_name='bedrock',
    region_name='us-west-2'  # Make sure this is a supported Bedrock region
)

def query_bedrock(model_id, input_text):
    response = bedrock.invoke_model(
        modelId=model_id,
        body={'text': input_text}  # Replace with the correct input format for Bedrock
    )
    # Process response based on Bedrock's response format
    output = response['body'].read().decode('utf-8')
    return output

    # Get user input
user_input = st.text_area("Enter your question or query:")

# Define model ID (make sure this is available in Bedrock)
model_id = "your-model-id"

# Button to trigger Bedrock API
if st.button("Get Answer"):
    if user_input:
        with st.spinner("Querying Amazon Bedrock..."):
            # Get response from Bedrock
            try:
                bedrock_response = query_bedrock(model_id, user_input)
                st.write("Response from Bedrock:")
                st.write(bedrock_response)
            except Exception as e:
                st.error(f"Error querying Bedrock: {e}")
    else:
        st.warning("Please enter some text to query.")