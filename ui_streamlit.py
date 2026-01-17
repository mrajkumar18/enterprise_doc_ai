import streamlit as st
from qa.rag_chain import get_rag_chain

# check access level
access_level = st.selectbox(
    "Access Level",
    options=["A1 - Full Access", "A2 - Limited Access", "A3 - View Only"]
)


st.set_page_config(
    page_title="Enterprise Document Intelligence",
    layout="wide"
)

st.title("Enterprise Document Intelligence")
st.caption("Document-grounded answers for policy, risk, and governance decisions")

@st.cache_resource
def load_chain():
    return get_rag_chain()

qa_chain = load_chain()

question = st.text_input(
    "Ask a business or compliance question",
    placeholder="e.g., What is the incident reporting timeline?"
)

if question:
    with st.spinner("Analyzing documents and generating answer..."):
        result = qa_chain(question)

    # Executive Answer Box
    # st.markdown("### Executive Summary")
    # st.success(result["result"])

    st.markdown("### Executive Summary")

    answer_text = result["result"]

    # STEP 4: Grade-based answer visibility
    if access_level.startswith("A3"):
     # Only first sentence for lower access
     answer_text = answer_text.split(".")[0] + "."

    if "contact the administrator" in answer_text.lower():
     st.warning(answer_text)
    else:
     st.success(answer_text)


    # Confidence indicator
    st.markdown("**Confidence:** Answer derived strictly from approved documents")

    # STEP 3: Decision Guidance (ADD HERE)
    st.markdown("### Decision Guidance")
    st.info(
        "Use this information to validate compliance requirements "
        "and confirm response timelines before taking action."
    )

    # Sources (collapsed by default)
    # with st.expander("View source documents"):
    #     for i, doc in enumerate(result["source_documents"], start=1):
    #         st.markdown(f"**Source {i}:** {doc.metadata.get('source', 'Unknown')}")
    #         st.write(doc.page_content[:500] + "...")


    # Sources - for production ready - source files hide
    # with st.expander("View source documents"):
    #     for i, doc in enumerate(result["source_documents"], start=1):
    #         st.markdown(f"**Source {i}:** {doc.metadata.get('source', 'Unknown')}")

    # sources - for role level access
    with st.expander("View source documents"):

        for i, doc in enumerate(result["source_documents"], start=1):
            source_name = doc.metadata.get("source", "Unknown")
            content = doc.page_content.strip()

            # A1: Full access
            if access_level.startswith("A1"):
                st.markdown(f"**Source {i}:** {source_name}")
                st.caption(content[:300] + "...")

            # A2: Partial access (first line only)
            elif access_level.startswith("A2"):
                first_line = content.split("\n")[0]
                st.markdown(f"**Source {i}:** {source_name}")
                st.caption(first_line)

            # A3: Minimal access (source name only)
            elif access_level.startswith("A3"):
                st.markdown(f"**Source {i}:** {source_name}")
        



