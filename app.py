import streamlit as st

from kleene import regex_to_nfa, accepts, get_transitions
from greedy import activity_selection   
from structural_hazard import simulate_pipeline, get_pipeline_table


st.set_page_config(
    page_title="Computer Science Concept Simulator",
    page_icon="🎓",
    layout="wide"
)


st.title("🎓 Computer Science Concept Simulator")

st.write(
    "An interactive micro-project demonstrating "
    "Kleene's Theorem, Greedy Algorithm and Structural Hazards."
)


st.divider()


tab1, tab2, tab3 = st.tabs(
    [
        "1️⃣ Kleene's Theorem",
        "2️⃣ Greedy Algorithm",
        "3️⃣ Structural Hazard"
    ]
)


# --------------------------------------------------
# MODULE 1 — KLEENE'S THEOREM
# --------------------------------------------------

with tab1:

    st.header("1. Kleene's Theorem")

    st.write(
        "This module demonstrates the relationship between "
        "Regular Expressions and Finite Automata."
    )

    st.info(
        "Enter a regular expression and test whether a string "
        "is accepted by the generated finite automaton."
    )

    regex = st.text_input(
        "Enter Regular Expression",
        value="(a|b)*"
    )

    test_string = st.text_input(
        "Enter String to Test",
        value="abba"
    )

    if st.button("Generate Automaton & Test", key="kleene_button"):

        try:

            nfa = regex_to_nfa(regex)

            transitions, start_state, accept_state = get_transitions(nfa)

            st.subheader("Finite Automaton")

            st.write(f"Start State: q{start_state}")
            st.write(f"Accept State: q{accept_state}")

            st.write("### Transition Table")

            for source, symbol, destination in transitions:

                st.write(
                    f"q{source}  -- {symbol} -->  q{destination}"
                )

            result = accepts(nfa, test_string)

            st.subheader("String Testing")

            st.write(f"Regular Expression: `{regex}`")
            st.write(f"Input String: `{test_string}`")

            if result:

                st.success(
                    f"✅ `{test_string}` is ACCEPTED"
                )

            else:

                st.error(
                    f"❌ `{test_string}` is REJECTED"
                )

        except Exception as error:

            st.error(f"Error: {error}")


# --------------------------------------------------
# MODULE 2 — GREEDY ALGORITHM
# --------------------------------------------------

with tab2:

    st.header("2. Greedy Algorithm")

    st.write(
        "Activity Selection Problem using the Greedy approach."
    )

    st.info(
        "Greedy Strategy: Always select the activity "
        "that finishes earliest."
    )

    st.subheader("Activities")

    activities = [
        ("A1", 1, 2),
        ("A2", 3, 4),
        ("A3", 0, 6),
        ("A4", 5, 7),
        ("A5", 8, 9),
    ]

    for name, start, finish in activities:

        st.write(
            f"**{name}** → Start: {start}, Finish: {finish}"
        )

    if st.button(
        "Run Greedy Algorithm",
        key="greedy_button"
    ):

        selected, steps = activity_selection(
            activities
        )

        st.subheader("Step-by-Step Selection")

        for step in steps:

            if step.startswith("Selected"):

                st.success(f"✅ {step}")

            else:

                st.warning(f"❌ {step}")

        st.subheader("Final Result")

        selected_names = [
            activity[0]
            for activity in selected
        ]

        st.write(
            "Selected Activities:",
            " → ".join(selected_names)
        )

        st.success(
            f"Maximum compatible activities: "
            f"{len(selected)}"
        )


# --------------------------------------------------
# MODULE 3 — STRUCTURAL HAZARD
# --------------------------------------------------

with tab3:

    st.header("3. Structural Hazard")

    st.write(
        "This module demonstrates structural hazards "
        "in a 5-stage processor pipeline."
    )

    st.info(
        "Pipeline stages: IF → ID → EX → MEM → WB"
    )

    st.subheader("Instructions")

    instructions = st.multiselect(
    "Select instructions in execution order:",
    ["LOAD", "COMPUTE", "STORE"],
    default=["LOAD", "COMPUTE", "COMPUTE", "LOAD"]
)

    if st.button(
        "Simulate Pipeline",
        key="hazard_button"
    ):

        if not instructions:

            st.warning(
                "Please select at least one instruction."
            )

        else:

            pipeline, hazards = simulate_pipeline(
                instructions
            )

            st.subheader("Pipeline Execution")

            table = get_pipeline_table(
                pipeline
            )

            st.table(table)

            st.subheader("Hazard Analysis")

            if hazards:

                for hazard in hazards:

                    st.error(
                        f"⚠️ {hazard}"
                    )

                st.warning(
                    "STALL inserted to resolve "
                    "the structural hazard."
                )

            else:

                st.success(
                    "✅ No structural hazard detected."
                )