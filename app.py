
# Import required libraries
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from sentence_transformers import SentenceTransformer, util
import torch
import streamlit as st

# Load GPT-2 Model and Tokenizer from Hugging Face Hub
def load_gpt2_model():
    model_name = 'gpt2'  # or 'gpt2-medium', 'gpt2-large', 'gpt2-xl'
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    tokenizer.pad_token = tokenizer.eos_token  # Set the padding token
    return model, tokenizer

model, tokenizer = load_gpt2_model()

# Load Sentence Transformer Model
embedder = SentenceTransformer('all-MiniLM-L6-v2')

# Expanded Knowledge Base

# expanded_knowledge_base = [
#     "Cybersecurity involves protecting computer systems from theft or damage to hardware, software, or data.",
#     "A security breach is an incident that results in unauthorized access to computer data, applications, networks, or devices.",
#     "Phishing is a method of trying to gather personal information using deceptive e-mails and websites.",
#     "Malware is software that is specifically designed to disrupt, damage, or gain unauthorized access to a computer system.",
#     "A firewall is a network security device that monitors and controls incoming and outgoing network traffic based on predetermined security rules.",
#     "Encryption is the process of converting information or data into a code, especially to prevent unauthorized access.",
#     "Two-factor authentication (2FA) is a security process in which the user provides two different authentication factors to verify themselves.",
#     "A Distributed Denial-of-Service (DDoS) attack is an attempt to make an online service unavailable by overwhelming it with traffic from multiple sources.",
#     "Social engineering is the use of deception to manipulate individuals into divulging confidential or personal information that may be used for fraudulent purposes.",
#     "Ransomware is a type of malware that threatens to publish the victim's personal data or perpetually block access to it unless a ransom is paid.",
#     "A VPN, or Virtual Private Network, extends a private network across a public network and enables users to send and receive data as if their devices were directly connected to the private network.",
#     "Intrusion detection systems (IDS) are devices or software applications that monitor a network for malicious activity or policy violations.",
#     "Zero-day vulnerabilities are software vulnerabilities that are unknown to the software vendor and have no patch or fix.",
#     "Penetration testing, also known as pen testing, is a simulated cyber attack against your computer system to check for exploitable vulnerabilities.",
#     "A security policy is a document that outlines how to protect an organization's physical and information technology assets.",
#     "Incident response is an organized approach to addressing and managing the aftermath of a security breach or cyberattack.",
#     "Threat intelligence is information about threats and threat actors that helps mitigate harmful events in cyberspace.",
#     "SIEM (Security Information and Event Management) solutions provide real-time analysis of security alerts generated by network hardware and applications.",
#     "Access control is a method of guaranteeing that users are who they say they are and that they have the appropriate access to company data.",
#     "An attack vector is a path or means by which a hacker can gain access to a computer or network server in order to deliver a payload or malicious outcome."
#     # Add more entries
# ]


expanded_knowledge_base = [
    "Cybersecurity involves protecting computer systems from theft or damage to hardware, software, or data.",
    "A security breach is an incident that results in unauthorized access to computer data, applications, networks, or devices.",
    "Phishing is a method of trying to gather personal information using deceptive e-mails and websites.",
    "Malware is software that is specifically designed to disrupt, damage, or gain unauthorized access to a computer system.",
    "A firewall is a network security device that monitors and controls incoming and outgoing network traffic based on predetermined security rules.",
    "Encryption is the process of converting information or data into a code, especially to prevent unauthorized access.",
    "Two-factor authentication (2FA) is a security process in which the user provides two different authentication factors to verify themselves.",
    "A Distributed Denial-of-Service (DDoS) attack is an attempt to make an online service unavailable by overwhelming it with traffic from multiple sources.",
    "Social engineering is the use of deception to manipulate individuals into divulging confidential or personal information that may be used for fraudulent purposes.",
    "Ransomware is a type of malware that threatens to publish the victim's personal data or perpetually block access to it unless a ransom is paid.",
    "A VPN, or Virtual Private Network, extends a private network across a public network and enables users to send and receive data as if their devices were directly connected to the private network.",
    "Intrusion detection systems (IDS) are devices or software applications that monitor a network for malicious activity or policy violations.",
    "Zero-day vulnerabilities are software vulnerabilities that are unknown to the software vendor and have no patch or fix.",
    "Penetration testing, also known as pen testing, is a simulated cyber attack against your computer system to check for exploitable vulnerabilities.",
    "A security policy is a document that outlines how to protect an organization's physical and information technology assets.",
    "Incident response is an organized approach to addressing and managing the aftermath of a security breach or cyberattack.",
    "Threat intelligence is information about threats and threat actors that helps mitigate harmful events in cyberspace.",
    "SIEM (Security Information and Event Management) solutions provide real-time analysis of security alerts generated by network hardware and applications.",
    "Access control is a method of guaranteeing that users are who they say they are and that they have the appropriate access to company data.",
    "An attack vector is a path or means by which a hacker can gain access to a computer or network server in order to deliver a payload or malicious outcome.",
    "Access Control List (ACL) is a list of permissions attached to an object, specifying which users or system processes can access the object and what operations they can perform.",
    "Botnet Command and Control (C2) is the infrastructure used by attackers to manage and control a network of compromised devices.",
    "Container Security refers to measures and tools used to secure containerized applications and environments from threats and vulnerabilities.",
    "Data Masking is the process of obscuring specific data within a database to protect it from unauthorized access while maintaining its usability.",
    "Denial of Service (DoS) Attack is an attack designed to shut down a machine or network, making it inaccessible to intended users by overwhelming it with traffic.",
    "Endpoint Detection and Response (EDR) provides continuous monitoring and response capabilities for endpoint devices.",
    "A Security Incident is any event that compromises the confidentiality, integrity, or availability of information or information systems.",
    "Network Access Control (NAC) technologies enforce policies for accessing a network, including authentication, authorization, and compliance checks.",
    "Decryption is the process of converting encrypted data back into its original, readable format.",
    "Network Address Translation (NAT) is a method used to modify network address information in packet headers while in transit across a traffic routing device.",
    "Threat Modeling is the process of identifying potential threats and vulnerabilities in a system and designing countermeasures to mitigate them.",
    "Business Continuity Plan (BCP) is a strategy for ensuring that critical business functions continue to operate in the event of a major disruption or disaster.",
    "Disaster Recovery Plan (DRP) is a documented process or set of procedures to recover and protect a business IT infrastructure in the event of a disaster.",
    "Penetration Testing Tools are software tools used by security professionals to simulate attacks and assess the security of a system or network (e.g., Metasploit, Burp Suite).",
    "Incident Command System (ICS) is a standardized approach to the command, control, and coordination of emergency response that integrates with incident response processes.",
    "A Security Patch is an update to software or hardware designed to fix security vulnerabilities or bugs.",
    "Security Token Service (STS) is a service that issues security tokens used to access resources or services in a secure manner.",
    "Patch Tuesday is the second Tuesday of each month when Microsoft releases security patches and updates for its products.",
    "Cybersecurity Insurance is a type of insurance coverage designed to help organizations mitigate financial losses from cyber incidents or breaches.",
    "Threat Landscape is the evolving environment of potential threats and vulnerabilities that organizations must navigate to protect their assets and information."
]


# Update Embeddings for the Expanded Knowledge Base
expanded_knowledge_embeddings = embedder.encode(expanded_knowledge_base, convert_to_tensor=True)

# Implement Retrieval-Augmented Generation
def retrieve_knowledge(query, knowledge_base, knowledge_embeddings, top_k=1):
    query_embedding = embedder.encode(query, convert_to_tensor=True)
    hits = util.semantic_search(query_embedding, knowledge_embeddings, top_k=top_k)
    relevant_info = knowledge_base[hits[0][0]['corpus_id']]
    return relevant_info

def generate_response_with_knowledge(query, model, tokenizer, knowledge_base, knowledge_embeddings):
    relevant_info = retrieve_knowledge(query, knowledge_base, knowledge_embeddings)
    combined_input = f"Relevant information: {relevant_info}\nResponse:"
    #\nUser query: {query}
    inputs = tokenizer(combined_input, return_tensors='pt')
    attention_mask = inputs.attention_mask
    outputs = model.generate(
        inputs.input_ids,
        attention_mask=attention_mask,
        max_length=100,  # Limit the max length of the generated text
        num_return_sequences=1,
        temperature=0.7,
        top_p=0.9,
        do_sample=True,  # Enable sampling
        pad_token_id=tokenizer.eos_token_id
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response.split("Response:")[1].strip()

# Create the Streamlit App
def main():
    st.title("Cybersecurity Risk Assessment Chatbot")

    # Initialize or get the conversation history from session state
    if 'history' not in st.session_state:
        st.session_state.history = []

    # Display conversation history
    for query, response in st.session_state.history:
        st.write(f"You: {query}")
        st.write(f"Chatbot: {response}")

    # Input for the new query
    user_input = st.text_input("You:", "")

    if st.button("Generate Response"):
        if user_input:
            response = generate_response_with_knowledge(user_input, model, tokenizer, expanded_knowledge_base, expanded_knowledge_embeddings)
            # Append new query and response to the history
            st.session_state.history.append((user_input, response))
            # Display the new response
            st.write(f"You: {user_input}")
            st.write(f"Chatbot: {response}")
        else:
            st.write("Please enter a query to get a response.")

if __name__ == "__main__":
    main()

