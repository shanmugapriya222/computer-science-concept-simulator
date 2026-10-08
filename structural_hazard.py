STAGES = ["IF", "ID", "EX", "MEM", "WB"]


def simulate_pipeline(instructions):
    """
    Simulate a simple 5-stage pipeline.

    Structural hazard:
    Instruction Fetch (IF) and Memory Access (MEM)
    share the same memory resource.

    If an instruction is using MEM while another
    instruction tries to use IF in the same cycle,
    a stall is inserted.
    """

    pipeline = []

    # Normal pipeline scheduling
    for index, instruction in enumerate(instructions):

        start_cycle = index + 1

        cycles = {}

        for stage_index, stage in enumerate(STAGES):
            cycles[start_cycle + stage_index] = stage

        pipeline.append({
            "instruction": instruction,
            "cycles": cycles
        })

    hazards = []

    # Check IF vs MEM conflicts
    for i in range(len(pipeline)):

        current = pipeline[i]

        for j in range(i + 1, len(pipeline)):

            other = pipeline[j]

            # Find IF cycle of later instruction
            other_if_cycle = None

            for cycle, stage in other["cycles"].items():

                if stage == "IF":
                    other_if_cycle = cycle
                    break

            # Find MEM cycle of earlier instruction
            current_mem_cycle = None

            for cycle, stage in current["cycles"].items():

                if stage == "MEM":
                    current_mem_cycle = cycle
                    break

            if (
                current_mem_cycle is not None
                and other_if_cycle is not None
                and current_mem_cycle == other_if_cycle
            ):

                # Shift the later instruction by one cycle
                shifted = {}

                for cycle, stage in other["cycles"].items():
                    shifted[cycle + 1] = stage

                # Insert STALL before IF
                shifted[other_if_cycle] = "STALL"

                other["cycles"] = shifted

                hazards.append(
                    f"Structural Hazard detected: "
                    f"{current['instruction']} uses MEM "
                    f"while {other['instruction']} needs IF "
                    f"in Cycle {current_mem_cycle}."
                )

                break

    return pipeline, hazards


def get_pipeline_table(pipeline):

    max_cycle = 0

    for instruction in pipeline:

        if instruction["cycles"]:
            max_cycle = max(
                max_cycle,
                max(instruction["cycles"].keys())
            )

    table = []

    for instruction in pipeline:

        row = {
            "Instruction": instruction["instruction"]
        }

        for cycle in range(1, max_cycle + 1):

            row[f"Cycle {cycle}"] = instruction[
                "cycles"
            ].get(cycle, "")

        table.append(row)

    return table