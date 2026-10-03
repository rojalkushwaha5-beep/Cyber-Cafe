
import streamlit as st
import socket

def ip():
    st.title("🔐 Cyber Security Cafe")

    choice = st.selectbox(
        "Choose your work",
        [
            "Find the IP address of websites",
            "Check Connection between server and port",
            "Detail information about the Websites including port"
        ]
    )

    # 1. Find IP Address
    if choice == "Find the IP address of websites":

        st.write("Enter your website domain")

        website = st.text_input("Example: google.com")

        if website:
            try:
                ip_address = socket.gethostbyname(website)
                st.success(f"IP Address: {ip_address}")

            except socket.gaierror:
                st.error("Invalid domain or domain could not be resolved.")

    # 2. Check Connection
    elif choice == "Check Connection between server and port":

        website = st.text_input("Enter the website name")

        port = st.number_input(
            "Enter the port number",
            min_value=1,
            max_value=65535,
            value=80,
            step=1
        )

        if st.button("Check Connection"):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(3)
                    result = s.connect_ex((website, int(port)))

                    if result == 0:
                        st.success(
                            f"Connected successfully to {website}:{port}"
                        )
                    else:
                        st.error(
                            f"Could not connect to {website}:{port}"
                        )

            except socket.gaierror:
                st.error("Invalid website/domain name.")

            except socket.timeout:
                st.error("Connection timed out.")

            except OSError as e:
                st.error(f"Connection error: {e}")

    # 3. Website Information
    elif choice == "Detail information about the Websites including port":

        website = st.text_input("Enter the website name")

        port = st.number_input(
            "Port number",
            min_value=1,
            max_value=65535,
            value=80,
            step=1
        )

        if st.button("Get Website Information"):
            try:
                info = socket.getaddrinfo(
                    website,
                    int(port),
                    type=socket.SOCK_STREAM
                )

                if not info:
                    st.warning("No information found.")
                else:
                    st.success("Information found successfully!")

                    for i, data in enumerate(info):

                        family = data[0]
                        sock_type = data[1]
                        protocol = data[2]
                        address = data[4]

                        st.subheader(f"Connection {i + 1}")

                        st.write("**Address Family:**", family)
                        st.write("**Socket Type:**", sock_type)
                        st.write("**Protocol:**", protocol)
                        st.write("**IP Address:**", address[0])
                        st.write("**Port:**", address[1])

            except socket.gaierror:
                st.error("Invalid website/domain name.")

            except OSError as e:
                st.error(f"Error: {e}")


if __name__ == "__main__":
    ip()
