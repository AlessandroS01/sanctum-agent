from langchain_core.messages import HumanMessage

from sanctum.graph.workflow import sanctum_graph


def run_session() -> None:
    session_id = "test-session-01"
    config = {"configurable": {"thread_id": session_id}}

    print("--- Sanctum Dialectical Sparring Engine ---\n")
    user_thesis = input("Enter a thesis to stress-test: ").strip()

    initial_state = {
        "thesis": user_thesis,
        "messages": [HumanMessage(content=user_thesis)],
        "concessions": [],
        "turn_count": 0,
    }

    # 1. Run until Steelman checkpoint
    print("\nFormulating steelman...")
    for event in sanctum_graph.stream(initial_state, config=config):
        for _, output in event.items():
            if "messages" in output:
                print(f"\n{output['messages'][-1].content}\n")

    print("[Checkpoint reached: Steelmanning complete]")
    approval = input(
        "Approve steelman? (Press Enter to accept, or type a correction): "
    ).strip()

    if approval:
        sanctum_graph.update_state(
            config,
            {"messages": [HumanMessage(content=f"Correction: {approval}")]},
        )

    # 2. Run initial Antithesis step
    print("\nBeginning cross-examination...")
    for event in sanctum_graph.stream(None, config=config):
        for _, output in event.items():
            if "messages" in output:
                print(f"\n[Inquisitor]:\n{output['messages'][-1].content}\n")

    # 3. Interactive conversational loop
    while True:
        snapshot = sanctum_graph.get_state(config)
        if not snapshot.next:
            print("\nDebate concluded.")
            break

        user_reply = input(
            "\nYour defense (or type 'conclude' to synthesize): "
        ).strip()
        if not user_reply:
            continue

        # Append human defense into the graph checkpoint
        sanctum_graph.update_state(
            config,
            {"messages": [HumanMessage(content=user_reply)]},
        )

        # Resume graph from current state
        for event in sanctum_graph.stream(None, config=config):
            for node_name, output in event.items():
                if "messages" in output:
                    speaker = "Synthesis" if node_name == "synthesis" else "Inquisitor"
                    print(f"\n[{speaker}]:\n{output['messages'][-1].content}\n")


if __name__ == "__main__":
    run_session()
