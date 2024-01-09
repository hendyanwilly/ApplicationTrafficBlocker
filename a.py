import subprocess

def block_program_firewall_rule(program_path):
    rule_name = "@hendyanwilly - ApplicationTrafficBlocker"
    rule_description = "by @hendyanwilly (github.com/hendyanwilly)"

    outbound_rule_command = [
        "netsh", "advfirewall", "firewall", "add", "rule",
        "name=" + rule_name,
        "description=" + rule_description,
        "program=" + program_path,
        "action=block",
        "dir=out"
    ]

    inbound_rule_command = [
        "netsh", "advfirewall", "firewall", "add", "rule",
        "name=" + rule_name,
        "description=" + rule_description,
        "program=" + program_path,
        "action=block",
        "dir=in"
    ]

    try:
        subprocess.run(outbound_rule_command, check=True)
        subprocess.run(inbound_rule_command, check=True)
    except subprocess.CalledProcessError as e:
        print("Error:", e)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    print("ApplicationTrafficBlocker\nby hendyanwilly (github.com/hendyanwilly)\n")

    program_path = input("Application path? ")
    program_path = program_path.replace('"', '')
    block_program_firewall_rule(program_path)
    input("Press enter to continue...")